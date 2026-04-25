from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = ROOT_DIR / "resources"


def resource_path(*parts: str) -> str:
    return str(RESOURCES_DIR.joinpath(*parts))
