#!/usr/bin/env python3
"""Demo ultra simple: ajoute les styles ASIT dans ArcGIS.

Pas de logique avancee:
- pas de check d'existence,
- pas de rapport local,
- script procedural (old school).
"""

import os
import sys

from arcgis.gis import GIS  # pyright: ignore[reportMissingImports]


# Parametres visibles en haut.
PORTAL_URL = os.getenv("ARCGIS_PORTAL_URL", "https://www.arcgis.com").strip()
USERNAME = os.getenv("ARCGIS_USERNAME", "").strip()
PASSWORD = os.getenv("ARCGIS_PASSWORD", "").strip()
VERIFY_CERT = os.getenv("ARCGIS_VERIFY_CERT", "true").strip().lower() != "false"
FOLDER = os.getenv("ARCGIS_FOLDER", "").strip() or None

# Limitation ArcGIS: pas de style hybride dans le script.
STYLE_URLS = [
    ("color", "https://vt.asit-asso.ch/styles/asit.color/style.json"),
    ("light", "https://vt.asit-asso.ch/styles/asit.light/style.json"),
    ("dark", "https://vt.asit-asso.ch/styles/asit.dark/style.json"),
]

EXTENT = "5.96,45.82,10.49,47.81"


if not USERNAME or not PASSWORD:
    print("ERROR: ARCGIS_USERNAME and ARCGIS_PASSWORD are required.", file=sys.stderr)
    print("Tip: copy .env.example and export values before running.", file=sys.stderr)
    sys.exit(2)

print(f"Connecting to {PORTAL_URL} as {USERNAME} (verify_cert={VERIFY_CERT})")
gis = GIS(PORTAL_URL, USERNAME, PASSWORD, verify_cert=VERIFY_CERT)

for style_key, style_url in STYLE_URLS:
    item = gis.content.add(
        item_properties={
            "type": "Vector Tile Service",
            "title": f"ASIT {style_key} style",
            "url": style_url,
            "snippet": "ASIT external vector tile style",
            "tags": ["asit", "vector-tiles", "style", style_key],
            "extent": EXTENT,
        },
        folder=FOLDER,
    )
    if item is None:
        raise RuntimeError(f"Failed to create item for style: {style_key}")
    print(f"[{style_key}] created: {item.id}")
