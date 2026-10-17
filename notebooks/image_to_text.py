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
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
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
        """Run OCR on every JPG image in a folder.

        The images are read in sorted filename order. Only files ending in
        ``.jpg`` (lowercase) are processed.

        Args:
            folder_path (str): The path to the folder that contains the JPG
                images.

        Returns:
            list[str]: The text extracted from each image, in the same order as
                the image files.
        """
        folder = Path(folder_path)

        image_files: list = sorted(folder.glob(pattern="*.jpg"))

        texts: list = []

        for image_file in image_files:
            text = pytesseract.image_to_string(image=Image.open(fp=image_file))
            texts.append(text)

        return texts

    def save_texts_to_file(texts: list[str], output_file: str) -> None:
        """Save OCR results to a text file, one block per image.

        Each block starts with a header line ``===== IMAGE n =====``, where
        ``n`` is the 1-based position of the text in the list, followed by the
        text and a blank line.

        Args:
            texts (list[str]): The OCR text of each image.
            output_file (str): The path of the text file to write. An existing
                file is overwritten.
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
