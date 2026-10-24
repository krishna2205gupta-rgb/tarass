# TARA Preview Setup

This repository contains the extracted **TARA** app from `TARAs.zip`.

## What this app is

- **Type:** FastAPI server app with a browser UI served from static files
- **Backend:** Python + FastAPI + Uvicorn
- **Frontend:** Static HTML/CSS/JavaScript (served by FastAPI)
- **Default preview port:** `8000`

## Zero-install browser preview (recommended)

1. Open in Codespaces: **https://codespaces.new/krishna2205gupta-rgb/tarass**
2. Wait for container setup to finish.
3. The devcontainer auto-starts the app and auto-opens forwarded port `8000`.

Preview URL format in Codespaces:

`https://<your-codespace-name>-8000.app.github.dev/`

## One-command run (local or remote shell)

```bash
pip install -r TARA-main/backend/requirements.txt
python run_preview.py
```

Then open: `http://127.0.0.1:8000/`
