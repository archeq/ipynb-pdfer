# ipynb-pdfer

A small Python utility to batch convert Jupyter notebooks (`.ipynb`) into PDF files.

The script scans `input/*.ipynb` and exports each notebook as PDF to `output/` using `nbconvert --to webpdf`.

## What this project does

- Converts every notebook matching `input/*.ipynb`.
- Uses `nbconvert` with the `webpdf` exporter.
- Checks whether `nbconvert`, `jupyter`, and `playwright` are installed.
- Installs missing Python packages with `pip`.
- Ensures Playwright Chromium is installed before conversion.

## Requirements

- Python `>=3.13,<3.14`
- Internet access on first run (for Python packages and Chromium download)

Project dependency declared in `pyproject.toml`:

- `nbconvert[webpdf]>=7.17.0`
- `playwright>=1.0.0`

## Setup

### Option 1: with `uv` (recommended)

```powershell
uv sync
```

### Option 2: with `pip`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

## How to run

1. Put notebook files into `input/`.
2. Run:

```powershell
python main.py
```

Runtime flow in `main.py`:

1. Prints a short platform greeting.
2. Checks `nbconvert`, `jupyter`, and `playwright` versions.
3. Installs any missing package via `python -m pip install <package>`.
4. Runs Playwright install for Chromium if browser cache is missing.
5. Converts all `input/*.ipynb` files to PDF in `output/`.

## Playwright browser path

The Chromium cache directory is resolved as follows:

1. `PLAYWRIGHT_BROWSERS_PATH` if set and not equal to `0`.
2. Otherwise platform default:
   - Windows: `%LOCALAPPDATA%\ms-playwright`
   - macOS: `~/Library/Caches/ms-playwright`
   - Linux: `~/.cache/ms-playwright`

## Folder layout

```text
ipynb-pdfer/
  main.py
  input/    # place .ipynb files here
  output/   # generated .pdf files appear here
```

## Quick example

If `input/` contains:

- `report.ipynb`
- `analysis.ipynb`

After running `python main.py`, `output/` should contain:

- `report.pdf`
- `analysis.pdf`
