from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List

class VectorStoreManager:
    """
    A class to manage the creation and usage of a FAISS-based vector store.
    """

    @staticmethod
    def create_vectorstore(docs: List[Document], embeddings) -> FAISS:
        """
        Create a FAISS vector store from documents and embeddings.

        Args:
            docs (List[Document]): A list of documents to store.
            embeddings: The embeddings model to use for vectorization.

        Returns:
            FAISS: A FAISS vector store instance.
        """
        try:
            return FAISS.from_documents(docs, embeddings)
        except Exception as e:
            raise RuntimeError(f"Failed to create vector store: {e}")

if __name__ == "__main__":
    # Example usage
    from sentence_transformers import SentenceTransformer
    from langchain.schema import Document

    # Sample documents
    documents = [
        Document(page_content="This is the first document."),
        Document(page_content="This is the second document."),
        Document(page_content="FAISS is great for vector search.")
    ]

    # Load embeddings model
    embeddings_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Create vector store
    vector_store = VectorStoreManager.create_vectorstore(documents, embeddings_model)
    print("Vector store created successfully.")