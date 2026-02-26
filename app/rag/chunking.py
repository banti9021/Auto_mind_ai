from typing import Generator

class TextChunker:
    """
    A class to handle chunking of text into smaller segments for processing.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        """
        Initialize the TextChunker class.

        Args:
            chunk_size (int): Maximum size of each chunk.
            overlap (int): Number of overlapping characters between chunks.
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> Generator[str, None, None]:
        """
        Split the text into chunks of specified size with overlap.

        Args:
            text (str): The input text to be chunked.

        Yields:
            str: A chunk of the text.
        """
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            yield text[start:end]
            start = end - self.overlap  # Move start with overlap

if __name__ == "__main__":
    # Example usage
    sample_text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
        "in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
    )

    chunker = TextChunker(chunk_size=100, overlap=20)
    print("Generated Chunks:")
    for i, chunk in enumerate(chunker.chunk_text(sample_text)):
        print(f"Chunk {i + 1}: {chunk}")