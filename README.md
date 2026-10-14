# PYNK Garment AI

Local-first garment processing backend with an optional future cloud worker.

## Quick start (Windows PowerShell)

```powershell
git clone https://github.com/DonnaMarie22/Pynk-Garment-ai.git
cd Pynk-Garment-ai
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Visit http://127.0.0.1:8000/docs and try GET /health.

This is a starter API only. No AI model, garment generator, remote access, or website connection is enabled yet. Keep the API bound to 127.0.0.1; do not expose it publicly.

## Architecture

- `app/main.py`: FastAPI endpoints.
- `app/processing.py`: local processing adapter; cloud adapter can be added later.
- `requirements.txt`: minimal dependencies.

Never commit private reference images, secrets, or model weights.
