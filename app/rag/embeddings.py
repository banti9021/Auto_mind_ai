from sentence_transformers import SentenceTransformer
from typing import List, Union, Generator  # Add Generator import

class EmbeddingGenerator:
    """
    A class to generate embeddings using the 'sentence-transformers/all-MiniLM-L6-v2' model.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the EmbeddingGenerator class.

        Args:
            model_name (str): Name of the pre-trained model to use. Defaults to 'sentence-transformers/all-MiniLM-L6-v2'.
        """
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def generate_embeddings(self, texts: Union[List[str], Generator[str, None, None]]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.

        Args:
            texts (Union[List[str], Generator[str, None, None]]): A list or generator of input texts to generate embeddings for.

        Returns:
            List[List[float]]: A list of embeddings, one for each input text.
        """
        if not isinstance(texts, list):
            texts = list(texts)  # Convert generator to list

        try:
            embeddings = self.model.encode(texts, convert_to_tensor=False)
            return embeddings
        except Exception as e:
            raise RuntimeError(f"Failed to generate embeddings: {e}")

if __name__ == "__main__":
    # Example usage
    texts = [
        "This is a test sentence.",
        "Sentence transformers are amazing!",
        "How do embeddings work?"
    ]

    generator = EmbeddingGenerator()
    embeddings = generator.generate_embeddings(texts)

    print("Generated Embeddings:")
    for i, embedding in enumerate(embeddings):
        print(f"Text {i + 1}: {texts[i]}")
        print(f"Embedding: {embedding[:5]}... (truncated)")