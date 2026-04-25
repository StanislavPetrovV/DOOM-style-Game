# Development

## Requirements

- Python 3.10 or newer recommended.
- Main dependency: `pygame`.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Recommended Organization

- Add new logic inside `game/`, not at the repository root.
- Keep `resources/` for runtime assets.
- Use `docs/` for architecture notes or gameplay mechanics.

## Minimal Verification

```bash
python -m compileall game main.py
```
