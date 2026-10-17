import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Imports
    """)
    return


@app.cell
def _():
    import whisper
    import pytube
    from pytube import YouTube

    return YouTube, pytube, whisper


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Functions
    """)
    return


@app.cell
def _(YouTube, pytube):
    def download_youtube_audio(url: str, output_path: str) -> None:
        """Downloads the audio of a YouTube video.

        Args:
            url (str): The URL of the YouTube video.
            output_path (str): The path to save the downloaded audio file.
        """
        try:
            # Creating a YouTube object
            yt = YouTube(url)

            # Extracting audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Downloading audio
            audio_stream.download(output_path=output_path)
            print("Audio downloaded successfully.")
        except (
            pytube.exceptions.RegexMatchError,
            pytube.exceptions.VideoUnavailable,
        ) as e:
            print(f"Error: {e}")

    def split_string_into_chunks(text: str, chunk_size: int = 2000) -> list:
        """Splits a string into chunks of approximately equal size, ensuring
        that words are not split.

        Args:
            text (str): The input string to split.
            chunk_size (int): The approximate size of each chunk. Default is
                2000.

        Returns:
            list: A list of strings where each element holds approximately 2000
                characters.
        """
        chunks = []
        current_chunk = ""

        words = text.split()  # Split text into words

        for word in words:
            # Check if adding the next word would exceed the chunk size
            if len(current_chunk) + len(word) + 1 <= chunk_size:  # Adding 1 for space
                current_chunk += word + " "
            else:
                chunks.append(current_chunk[:-1])  # Remove the trailing space
                current_chunk = word + " "

        # Add the remaining chunk if any
        if current_chunk:
            chunks.append(current_chunk[:-1])  # Remove the trailing space

        return chunks

    def merge_text_with_timestamp(data: list[dict[str, str]]) -> str:
        """Merge text with corresponding timestamps into a single string.

        Args:
            data (List[Dict[str, str]]): A list of dictionaries containing
                'start' key specifying start time and 'text' key containing a
                sentence.

        Returns:
            str: A single string where each sentence is preceded by its
                corresponding timestamp in the format "m:ss.s".

        Example:
            data = [ {'start': '0.00', 'text': 'This is the first sentence.'},
            {'start': '1.23', 'text': 'This is the second sentence.'}, {'start':
            '3.45', 'text': 'This is the third sentence.'} ] merged_text =
            merge_text_with_timestamp(data) print(merged_text) # Output: #
            [0:00.0] This is the first sentence. [0:01.2] This is the second
            sentence. [0:03.5] This is the third sentence.
        """
        merged_text = ""
        for entry in data:
            timestamp = float(entry["start"])
            minutes = int(timestamp / 60)
            seconds = timestamp % 60
            formatted_timestamp = f"[{minutes}m{seconds:.1f}s] "
            merged_text += formatted_timestamp + entry["text"] + " "
        merged_text = " ".join(merged_text.split())

        return merged_text.strip()

    return merge_text_with_timestamp, split_string_into_chunks


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Load model
    """)
    return


@app.cell
def _(whisper):
    model = whisper.load_model("large")
    return (model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pipeline
    """)
    return


@app.cell
def _():
    # Download audio file from youtube.
    url = "https://www.youtube.com/watch?v=gS9PWbQuKsU"  # noqa: F841
    output_path = "change/this/path"
    output_path = output_path.replace("\\", "/")

    # download_youtube_audio(
    #     url=url,
    #     output_path=output_path
    # )
    return (output_path,)


@app.cell
def _(model, output_path):
    # Transcribe the audio file
    audio_file_name = "interview.aac"
    audio_file_path = f"{output_path}/{audio_file_name}"
    result = model.transcribe(audio_file_path, language="dutch")
    return (result,)


@app.cell
def _(result):
    transcript = result["text"]  # noqa: F841
    return


@app.cell
def _(merge_text_with_timestamp, result):
    transcript_with_all_timestamps = merge_text_with_timestamp(result["segments"])
    for char in transcript_with_all_timestamps:
        if char == "[":
            print("")
        print(char, end="")
    return (transcript_with_all_timestamps,)


@app.cell
def _(split_string_into_chunks, transcript_with_all_timestamps):
    # Convert to chunks.
    transcript_chunks = split_string_into_chunks(transcript_with_all_timestamps)
    return (transcript_chunks,)


@app.cell
def _(transcript_chunks):
    # Display chunks.
    i = 0
    for chunk in transcript_chunks:
        print(i)
        print(chunk)
        print("\n")
        i += 1
    return


if __name__ == "__main__":
    app.run()
