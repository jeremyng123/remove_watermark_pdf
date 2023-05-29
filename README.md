# Removing Watermark from PDFs

I made this repository to remove watermarks from PDFs.

## Installation
Create a new virtual environment with Python:

```sh
python -m venv $python_env
```

Install all the packages required for this project (yapf is included because I like yapf formatting. Feel free to remove this)

```sh
pip install -r requirements.txt
```

## Usage
```sh
python remove_watermark.py filename.pdf watermark_subtext
```