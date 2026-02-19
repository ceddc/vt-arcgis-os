# Styles ASIT dans ArcGIS (contournement simple)

Ce depot propose un contournement simple, car ArcGIS Online ne permet pas nativement d'ajouter directement des styles de tuiles vectorielles externes depuis l'interface.

## URLs des styles ASIT

- Couleur: `https://vt.asit-asso.ch/styles/asit.color/style.json`
- Clair: `https://vt.asit-asso.ch/styles/asit.light/style.json`
- Sombre: `https://vt.asit-asso.ch/styles/asit.dark/style.json`
- Hybride: `https://vt.asit-asso.ch/styles/asit.hybrid/style.json`

Note: ArcGIS ne gere pas correctement le style hybride dans ce flux. Le script Python n'ajoute donc que `color`, `light` et `dark`.

## Contournement manuel dans ArcGIS Online

1. Télécharger le JSON du style souhaité.
2. Ouvrir le Vector Tile Style Editor.
3. Créer et enregistrer un nouveau style dans votre organisation à partir de n'importe quel style de la liste proposée.
4. Une fois le style sauvegardé, ouvrir l'élément correspondant et cliquer sur « Mettre à jour ».
5. Téléverser le JSON du style.

## Automatisation Python (ArcGIS API for Python)

Script: `scripts/add_asit_styles.py`

Ce que fait le script:
- Se connecte à ArcGIS Online (par défaut `https://www.arcgis.com`) ou ArcGIS Enterprise.
- Crée des items `Vector Tile Service` à partir des URLs de styles ASIT.
- Reste volontairement minimal (pas de vérification des doublons, pas de rapport d'exécution).

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Variables d'environnement (ne pas commiter de secrets)

```bash
export ARCGIS_PORTAL_URL="https://www.arcgis.com"
export ARCGIS_USERNAME="votre_utilisateur"
export ARCGIS_PASSWORD="votre_mot_de_passe"
export ARCGIS_VERIFY_CERT="true"
# optionnel
export ARCGIS_FOLDER=""
```

### Exécution

```bash
python scripts/add_asit_styles.py
```

## Remarques

- Les identifiants sont lus uniquement via des variables d'environnement.
- `.env` est ignoré par git.
- Compatible ArcGIS Online et ArcGIS Enterprise (adapter `ARCGIS_PORTAL_URL`).
