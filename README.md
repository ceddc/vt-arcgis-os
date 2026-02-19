# ASIT styles in ArcGIS (simple workaround)

This repository provides a simple workaround because ArcGIS Online does not expose a direct UI flow to add external vector tile styles as reusable style items.

## ASIT style URLs

- Color: `https://vt.asit-asso.ch/styles/asit.color/style.json`
- Light: `https://vt.asit-asso.ch/styles/asit.light/style.json`
- Dark: `https://vt.asit-asso.ch/styles/asit.dark/style.json`
- Hybrid: `https://vt.asit-asso.ch/styles/asit.hybrid/style.json`

Note: ArcGIS ne gere pas correctement le style hybride dans ce flux. Le script Python n'ajoute donc que `color`, `light` et `dark`.

## ArcGIS Online UI workaround (manual)

1. Open Vector Tile Style Editor.
2. Create and save any new style in your organization.
3. Open the saved item and click update style.
4. Replace the style URL with one of the ASIT URLs above.

## Python automation (ArcGIS API for Python)

Script: `scripts/add_asit_styles.py`

What it does:
- Connects to ArcGIS Online (default `https://www.arcgis.com`) or ArcGIS Enterprise.
- Creates `Vector Tile Service` items from ASIT style URLs.
- Keeps the script intentionally minimal (no duplicate check, no run report file).

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Environment variables (do not commit secrets)

```bash
export ARCGIS_PORTAL_URL="https://www.arcgis.com"
export ARCGIS_USERNAME="your_username"
export ARCGIS_PASSWORD="your_password"
export ARCGIS_VERIFY_CERT="true"
# optional
export ARCGIS_FOLDER=""
```

### Run

```bash
python scripts/add_asit_styles.py
```

## Notes

- Credentials are read from environment variables only.
- `.env` is ignored by git.
- Works for ArcGIS Online and ArcGIS Enterprise (set `ARCGIS_PORTAL_URL` accordingly).
