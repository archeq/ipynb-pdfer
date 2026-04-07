# ipynb-pdfer

A small Python utility to **mass convert Jupyter notebooks (`.ipynb`) into PDF files**.

It scans all notebooks in `input/` and exports each one as PDF into `output/`.

## What this project does

- Batch-converts every `input/*.ipynb` file.
- Uses `nbconvert` with the `webpdf` exporter.
- Writes generated PDFs into `output/`.

## Requirements

- Python `>=3.13,<3.14`
- Windows recommended (the script includes Windows-specific `winget` install steps)
- Internet access on first run (for dependency/tool installation)

Project dependency (from `pyproject.toml`):

- `nbconvert[webpdf]>=7.17.0`

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

1. Put your notebook files in `input/`.
2. Run the script:

```powershell
python main.py
```

The script will:

- Try to install `pandoc` (via `winget`) if missing.
- Try to install MiKTeX (`xelatex`) (via `winget`) if missing.
- Ensure `nbconvert` and `jupyter` are installed.
- Convert all notebooks from `input/` to PDFs in `output/`.

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

After running, `output/` should contain:

- `report.pdf`
- `analysis.pdf`

