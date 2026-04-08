import glob
import importlib.metadata as md
from pathlib import Path
import os
import platform
import subprocess
import sys


def install(package):
    """Installs a given package with pip.
        Args:
            package (str): Name of a package to install.
        Returns:
            None
        Raises:
            subprocess.CalledProcessError: If pip installation fails.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def get_package_version(dist_name: str) -> str | None:
    """Checks, whether a package is installed.
    Args:
        dist_name (str): Name of a package in string format.
    Returns:
        str | None: Package version, if it is installed;
        None, otherwise.
    """
    try:
        return md.version(dist_name)
    except md.PackageNotFoundError:
        return None


def convert_to_pdf():
    """Convert all notebooks from `input/` to PDF files in `output/`.

    Uses `nbconvert` with the `webpdf` exporter for each `.ipynb` file found
    by the `input/*.ipynb` glob pattern.

    Raises:
        subprocess.CalledProcessError: If `nbconvert` fails for any notebook.
    """
    for notebook in glob.glob('input/*.ipynb'):
        subprocess.check_call([sys.executable, "-m", "nbconvert", "--to", "webpdf", notebook, "--output-dir", "output"])

def playwright_browser_root() -> Path:
    """Return the expected Playwright browser cache directory.

    The value is resolved in this order:
    1. `PLAYWRIGHT_BROWSERS_PATH` (if set and not equal to "0").
    2. Platform default cache location.

    Returns:
        Path: Filesystem path where Playwright-managed browser binaries are
        expected to be stored.
    """
    custom = os.environ.get("PLAYWRIGHT_BROWSERS_PATH")
    if custom and custom != "0":
        return Path(custom).expanduser()

    if platform.system() == "Windows":
        return Path(os.environ.get("LOCALAPPDATA", Path.home())) / "ms-playwright"
    if platform.system() == "Darwin":
        return Path.home() / "Library" / "Caches" / "ms-playwright"
    return Path.home() / ".cache" / "ms-playwright"

def ensure_chromium():
    """Ensure a Playwright Chromium build is installed.

    If the browser root directory does not exist, installs Chromium (and OS
    dependencies when required) via Playwright CLI.

    Raises:
        subprocess.CalledProcessError: If Playwright browser installation fails.
    """
    root = playwright_browser_root()
    if not root.exists():
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "--with-deps","chromium"])
    else:
        print("Chromium already installed")
        return


if __name__ == "__main__":
    if platform.system() == "Windows":
        print("Welcome on", platform.system())

    elif platform.system() == "Linux":
        print("Welcome on Pingwin")

    pkgs = ["nbconvert", "jupyter", "playwright"]
    for pkg in pkgs:
        version = get_package_version(pkg)
        if version:
            print(f"{pkg} installed: {version}")
        else:
            print(f"{pkg} not installed")
            install(pkg)
    ensure_chromium()
    convert_to_pdf()
