from fastapi import FastAPI
from app.processing import available_backends

app = FastAPI(title="PYNK Garment AI", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "pynk-garment-ai"}


@app.get("/backends")
def backends() -> dict[str, dict[str, bool]]:
    return {"available": available_backends()}
