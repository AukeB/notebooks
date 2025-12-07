import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Book translation
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
    import re
    import string

    import marimo as mo

    from ebooklib import epub
    from collections import defaultdict
    from lingua import Language, LanguageDetectorBuilder
    return Language, LanguageDetectorBuilder, defaultdict, epub, mo, re, string


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Functions
    """)
    return


@app.cell
def _(Language, LanguageDetectorBuilder, defaultdict, epub, re, string):
    def read_epub_file(epub_file_path: str):
        """
        Reads an EPUB file and returns an EPUB book object.

        Args:
            epub_file_path (str): Path to the EPUB file.

        Returns:
            EPUB: The loaded EPUB book object if successful, otherwise None.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            Exception: For any other error that occurs during file reading.
        """
        try:
            return epub.read_epub(epub_file_path)
        except FileNotFoundError:
            raise
        except Exception:
            return None

    def extract_epub_text(book):
        """
        Extracts and returns all text content from an EPUB book object.

        Args:
            book (EPUB): The loaded EPUB book object.

        Returns:
            str: The concatenated text content from all HTML items in the book.
        """
        text = ''

        for item in book.get_items():
            if isinstance(item, epub.EpubHtml):
                text += item.get_content().decode('utf-8')

        return text

    def process_text_to_word_counts(text: str) -> dict:
        """
        Cleans text, extracts words, and returns a dictionary of word counts
        sorted by frequency in descending order.

        Args:
            text (str): The raw text to process.

        Returns:
            dict: A dictionary where keys are unique words and values are their
                respective counts, sorted by count in descending order.
        """
        cleaned_text = re.sub('<.*?>', '', text)
        cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))
        word_list = cleaned_text.split()

        word_counts = defaultdict(int)
        for word in word_list:
            word_counts[word] += 1

        sorted_dict = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
        return sorted_dict

    def exclude_english_words(word_counts: dict[str, int]) -> dict[str, int]:
        """
        Detects and filters out English words from a dictionary of word counts,
        returning only the German words based on language confidence scores.

        Args:
            word_counts (dict): A dictionary where keys are words and values are
                their occurrence counts.

        Returns:
            dict: A dictionary containing only German words and their counts.
        """
        languages = [Language.ENGLISH, Language.GERMAN]
        detector = LanguageDetectorBuilder.from_languages(*languages).build()

        german_word_counts = {}

        for word, count in word_counts.items():
            confidence_values = detector.compute_language_confidence_values(word)
            for confidence_value in confidence_values:
                if confidence_value.language.name == 'GERMAN' and confidence_value.value >= 0.5:
                    german_word_counts[word] = count
                    break

        return german_word_counts
    return (
        exclude_english_words,
        extract_epub_text,
        process_text_to_word_counts,
        read_epub_file,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Workflow
    """)
    return


@app.cell
def _():
    epub_file_path: str = "data/other/siddhartha_eine_indische_dichtung_herman_hesse.epub"
    return (epub_file_path,)


@app.cell
def _(
    epub_file_path: str,
    exclude_english_words,
    extract_epub_text,
    process_text_to_word_counts,
    read_epub_file,
):
    book = read_epub_file(epub_file_path=epub_file_path)

    epub_content = extract_epub_text(book=book)
    unique_words_with_counts = process_text_to_word_counts(text=epub_content)

    print(f"- There are {len(unique_words_with_counts)} unique words in this .epub file.")

    unique_german_words = exclude_english_words(word_counts=unique_words_with_counts)

    print(f"- After excluding English words, there are {len(unique_german_words)} unique German words left.")

    print("- 10 most occuring words:\n")
    for i, (k, v) in enumerate(unique_german_words.items()):
        if i < 10:
            print({k: v})
    return


if __name__ == "__main__":
    app.run()
