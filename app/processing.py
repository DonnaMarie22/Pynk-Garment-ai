from typing import Literal

Backend = Literal["local", "cloud"]


def available_backends() -> dict[str, bool]:
    """Cloud processing is intentionally disabled until configured securely."""
    return {"local": True, "cloud": False}
