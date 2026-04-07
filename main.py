import glob
import importlib.metadata as md
import platform
import shutil
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
    """Converts given IPYNB files into .pdf.
        Args:
            None;
        Returns:
            None;
        Raises:
            ...
    """
    for notebook in glob.glob('input/*.ipynb'):
        subprocess.check_call([sys.executable, "-m", "nbconvert", "--to", "webpdf", notebook, "--output-dir", "output"])


if __name__ == "__main__":
    if platform.system() == "Windows":
        print("Welcome on", platform.system())

    if shutil.which("pandoc") is None:
        try:
            subprocess.run(["winget", "install", "--id", "JohnMacFarlane.Pandoc", "-e"], check=True)
        except subprocess.CalledProcessError:
            print("Failed to install Pandoc.")

    if shutil.which("xelatex") is None:
        try:
            subprocess.run(["winget", "install", "--id", "MiKTeX.MiKTeX", "-e"], check=True)
        except subprocess.CalledProcessError:
            print("Failed to install MikTeX.")

    pkgs = ["nbconvert", "jupyter"]
    for pkg in pkgs:
        version = get_package_version(pkg)
        if version:
            print(f"{pkg} installed: {version}")
        else:
            print(f"{pkg} not installed")
            install(pkg)
    convert_to_pdf()
