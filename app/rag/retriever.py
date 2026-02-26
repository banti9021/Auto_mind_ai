from langchain_community.vectorstores import FAISS

class RetrieverManager:
    """
    A class to manage retrievers from vector stores.
    """

    @staticmethod
    def get_retriever(vectorstore: FAISS):
        """
        Create a retriever from a vector store.

        Args:
            vectorstore (FAISS): The FAISS vector store instance.

        Returns:
            A retriever instance from the vector store.
        """
        try:
            return vectorstore.as_retriever()
        except Exception as e:
            raise RuntimeError(f"Failed to create retriever: {e}")

if __name__ == "__main__":
    # Example usage
    from sentence_transformers import SentenceTransformer
    from langchain.schema import Document
    from langchain_community.vectorstores import FAISS

    # Sample documents
    documents = [
        Document(page_content="This is the first document."),
        Document(page_content="This is the second document."),
        Document(page_content="FAISS is great for vector search.")
    ]

    # Load embeddings model
    embeddings_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Create vector store
    vector_store = FAISS.from_documents(documents, embeddings_model)

    # Create retriever
    retriever = RetrieverManager.get_retriever(vector_store)
    print("Retriever created successfully.")