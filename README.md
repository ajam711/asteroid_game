# Asteroid Game

A simple Asteroids clone built with Python and [pygame](https://www.pygame.org/).

## Requirements

- Python >= 3.13 (pinned in [.python-version](.python-version))
- [uv](https://docs.astral.sh/uv/) for dependency and Python version management

## Setup

### 1. Install uv (if you don't already have it)

macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or via pip, if you prefer:

```bash
pip install uv
```

### 2. Install Python

If you don't have a compatible Python version installed, let `uv` install it for you:

```bash
uv python install 3.13
```

To install an older/different version instead (e.g. if you need to override the pin):

```bash
uv python install 3.11
uv python pin 3.11
```

### 3. Install project dependencies

Creates `.venv` and installs everything from `uv.lock`:

```bash
uv sync
```

## Managing dependencies

Add a new dependency:

```bash
uv add <package>
```

Remove a dependency:

```bash
uv remove <package>
```

Upgrade a dependency:

```bash
uv lock --upgrade-package <package>
```

## Run

```bash
uv run main.py
```

## Controls

| Key   | Action          |
|-------|-----------------|
| W     | Move forward    |
| S     | Move backward   |
| A     | Rotate left     |
| D     | Rotate right    |
| Space | Shoot           |

## Gameplay

- Asteroids spawn and drift across the screen.
- Shooting an asteroid splits it into smaller ones until it's below the minimum size, then it's destroyed.
- Colliding with an asteroid ends the game.

## Roadmap

See [IDEAS.md](IDEAS.md) for planned features (scoring, lives, power-ups, screen wrapping, etc.).
