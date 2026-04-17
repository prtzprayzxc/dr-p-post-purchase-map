"""
Pull all offers from Kajabi Admin API and dump to JSON + CSV.

Auth: OAuth2 client_credentials (API Key = client_id, API Secret = client_secret)
Base URL: https://api.kajabi.com/v1
Docs: https://developers.kajabi.com/

Usage:
    python scripts/kajabi/pull_offers.py
Outputs:
    scripts/kajabi/output/offers.json
    scripts/kajabi/output/offers.csv
    scripts/kajabi/output/products.json
"""

from __future__ import annotations

import base64
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://api.kajabi.com/v1"
TOKEN_URL = f"{BASE_URL}/oauth/token"

ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = ROOT / ".env"
OUT_DIR = Path(__file__).resolve().parent / "output"


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        sys.exit(f"[ERROR] .env not found at {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


UA = "DrP-Automation/1.0 (+python-urllib)"


def http_post_form(url: str, data: dict[str, str]) -> dict:
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "User-Agent": UA,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_get_json(url: str, token: str) -> dict:
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "User-Agent": UA,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _token_via_basic(client_id: str, client_secret: str) -> dict:
    creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    body = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()
    req = urllib.request.Request(
        TOKEN_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "User-Agent": UA,
            "Authorization": f"Basic {creds}",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _token_via_body(client_id: str, client_secret: str) -> dict:
    return http_post_form(
        TOKEN_URL,
        {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )


def get_access_token(client_id: str, client_secret: str) -> str:
    print(f"[auth] requesting token from {TOKEN_URL}")
    last_err = None
    for method, fn in (("basic", _token_via_basic), ("body", _token_via_body)):
        try:
            print(f"[auth] trying {method} auth")
            payload = fn(client_id, client_secret)
            token = payload.get("access_token")
            if token:
                print(f"[auth] OK via {method} (expires_in={payload.get('expires_in')})")
                return token
            last_err = f"no access_token in response: {payload}"
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            last_err = f"{method} auth: {e.code} {body}"
            print(f"[auth] {method} failed: {e.code}")
    sys.exit(f"[ERROR] all auth methods failed. last: {last_err}")


def paginate(endpoint: str, token: str, page_size: int = 100) -> list[dict]:
    items: list[dict] = []
    page = 1
    while True:
        qs = urllib.parse.urlencode({"page[number]": page, "page[size]": page_size})
        url = f"{BASE_URL}{endpoint}?{qs}"
        print(f"[fetch] {url}")
        try:
            payload = http_get_json(url, token)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            sys.exit(f"[ERROR] GET {endpoint} failed {e.code}: {body}")
        data = payload.get("data", [])
        items.extend(data)
        meta = payload.get("meta", {}) or {}
        page_count = (
            meta.get("page_count")
            or meta.get("total_pages")
            or (payload.get("links", {}) or {}).get("last")
        )
        if not data or len(data) < page_size:
            break
        if isinstance(page_count, int) and page >= page_count:
            break
        page += 1
        if page > 50:
            print("[warn] pagination cutoff at 50 pages")
            break
    return items


def flatten_offer(o: dict) -> dict:
    attrs = o.get("attributes", {}) or {}
    rels = o.get("relationships", {}) or {}
    product_rels = ((rels.get("products") or {}).get("data")) or []
    return {
        "id": o.get("id"),
        "title": attrs.get("title") or attrs.get("name"),
        "status": attrs.get("status"),
        "price_in_cents": attrs.get("price_in_cents") or attrs.get("price"),
        "currency": attrs.get("currency"),
        "offer_type": attrs.get("offer_type") or attrs.get("type"),
        "created_at": attrs.get("created_at"),
        "updated_at": attrs.get("updated_at"),
        "checkout_url": attrs.get("checkout_url"),
        "product_count": len(product_rels),
        "product_ids": ",".join(str(p.get("id")) for p in product_rels),
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> None:
    env = load_env(ENV_PATH)
    key = env.get("KAJABI_API_KEY", "")
    secret = env.get("KAJABI_API_SECRET", "")
    if not key or not secret:
        sys.exit("[ERROR] KAJABI_API_KEY or KAJABI_API_SECRET missing in .env")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    token = get_access_token(key, secret)

    offers = paginate("/offers", token)
    products = paginate("/products", token)

    (OUT_DIR / "offers.json").write_text(
        json.dumps(offers, indent=2), encoding="utf-8"
    )
    (OUT_DIR / "products.json").write_text(
        json.dumps(products, indent=2), encoding="utf-8"
    )
    write_csv(OUT_DIR / "offers.csv", [flatten_offer(o) for o in offers])

    print()
    print(f"[done] offers: {len(offers)}  |  products: {len(products)}")
    print(f"[done] wrote {OUT_DIR}/offers.json, offers.csv, products.json")


if __name__ == "__main__":
    main()
