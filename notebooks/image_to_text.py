import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Image to text

    Notebook for converting images to text using Tesseract OCR
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Imports
    """)
    return


@app.cell
def _():
    import marimo as mo

    import pytesseract

    from pathlib import Path
    from PIL import Image

    return Image, Path, mo, pytesseract


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Settings
    """)
    return


@app.cell
def _(pytesseract):
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract" # ty: ignore
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Functions
    """)
    return


@app.cell
def _(Image, Path, pytesseract):
    def extract_texts_from_folder(folder_path: str) -> list[str]:
        """
        Load all JPG files in a folder, sorted by filename,
        perform OCR, and return a list of extracted strings.
        """
        folder = Path(folder_path)

        image_files: list[Path] = sorted(folder.glob(pattern="*.jpg"))

        texts: list = []

        for image_file in image_files:
            text = pytesseract.image_to_string(image=Image.open(fp=image_file))
            texts.append(text)

        return texts
    def save_texts_to_file(texts: list[str], output_file: str) -> None:
        """
        Save a list of OCR strings to a text file.
        """
        with open(output_file, mode="w", encoding="utf-8") as f:
            for i, text in enumerate(texts, start=1):
                f.write(f"===== IMAGE {i} =====\n")
                f.write(text)
                f.write("\n\n")

    return extract_texts_from_folder, save_texts_to_file


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Run
    """)
    return


@app.cell
def _(extract_texts_from_folder, save_texts_to_file):
    texts: list[str] = extract_texts_from_folder(folder_path="../temp")
    save_texts_to_file(texts, output_file="../temp/ocr_output.txt")
    return


if __name__ == "__main__":
    app.run()
