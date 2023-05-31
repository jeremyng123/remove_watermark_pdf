# Removing Watermark from PDFs

I made this repository to remove watermarks from PDFs.


# Disclaimer
The information and tools provided here are intended for use only on PDF files for which you have the **necessary legal rights to alter or change**. The removal of watermarks or other copyright notices should only be done with **explicit permission from the copyright holder**. Any misuse of the information and tools provided, including, but not limited to, the unauthorized removal of watermarks or other copyright notices, is strictly prohibited and may be ***_illegal_***.

The user assumes all liability and responsibility for their actions in utilizing the information and tools provided, and agrees to indemnify and hold harmless the provider of this information and tools for any and all claims arising from the user's activities.


## Installation
Create a new virtual environment with Python:

```sh
python -m venv $python_env
```

Install all the packages required for this project (yapf is included because I like yapf formatting. Feel free to remove this)

```sh
pip install -r requirements.txt
```

> If you want to execute the code using IPython Notebook on VSCode, use `requirements_ipynb.txt` instead.
> ```sh
> pip install -r requirements_ipynb.txt
> ```

## Usage
```sh
python remove_watermark.py input_filename.pdf output_filename.pdf
```
