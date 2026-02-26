from typing import Generator
from agents.executor import TaskExecutor
from agents.planner import TaskPlanner
from agents.graph import GraphManager
from rag.loader import DataLoader
from rag.chunking import TextChunker
from rag.embeddings import EmbeddingGenerator
from rag.vector_store import VectorStoreManager
from rag.retriever import RetrieverManager
from tools.search_tool import SearchTool
from langchain.schema import Document
from sentence_transformers import SentenceTransformer


def main():
    # Initialize components
    print("Initializing components...")
    data_loader = DataLoader()
    chunker = TextChunker(chunk_size=100, overlap=20)
    embedding_generator = EmbeddingGenerator()
    graph_manager = GraphManager()
    executor = TaskExecutor()
    planner = TaskPlanner(executor, graph_manager)
    search_tool = SearchTool(api_key="your_api_key_here")  # Replace with actual API key

    # Load and process data
    print("Loading data...")
    pdf_files = data_loader.list_files(extensions=[".pdf"])
    print(f"Found {len(pdf_files)} PDF files.")

    for pdf_file in pdf_files:
        print(f"Processing file: {pdf_file}")
        # Example: Load file content (assuming text-based PDFs)
        content = data_loader.load_file(pdf_file)

        # Process chunks one at a time to avoid MemoryError
        print("Generating embeddings...")
        documents = []
        for chunk in chunker.chunk_text(content):
            embedding = embedding_generator.generate_embeddings([chunk])  # Process one chunk at a time
            documents.append(Document(page_content=chunk))

        # Create vector store
        print("Creating vector store...")
        vector_store = VectorStoreManager.create_vectorstore(documents, embedding_generator.model)

        # Create retriever
        print("Creating retriever...")
        retriever = RetrieverManager.get_retriever(vector_store)

        # Example: Search and retrieve
        query = "Example query"
        print(f"Searching for: {query}")
        results = retriever.get_relevant_documents(query)
        print("Search Results:")
        for result in results:
            print(result.page_content)

    # Example: Task planning and execution
    print("Planning and executing tasks...")

    def example_task():
        print("Example task executed.")

    executor.register_task("ExampleTask", example_task)
    planner.add_task("ExampleTask")
    planner.execute_plan()

if __name__ == "__main__":
    main()