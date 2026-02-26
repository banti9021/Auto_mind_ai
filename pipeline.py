from app.agents.executor import Executor
from app.llm.local_llm import LocalLLM
from app.memory.memory import Memory
from app.rag.retriever import Retriever
from app.tools.search_tool import SearchTool
from app.utils.logger import Logger

# Initialize logger
logger = Logger()

# Initialize components
logger.info("Initializing components...")
executor = Executor()
llm = LocalLLM()
memory = Memory()
retriever = Retriever()
search_tool = SearchTool()

# Define the pipeline function
def run_pipeline(input_data):
    logger.info("Starting pipeline...")

    # Step 1: Retrieve relevant information
    logger.info("Retrieving relevant information...")
    retrieved_data = retriever.retrieve(input_data)

    # Step 2: Process data with memory
    logger.info("Processing data with memory...")
    memory_data = memory.process(retrieved_data)

    # Step 3: Generate response using LLM
    logger.info("Generating response using LLM...")
    response = llm.generate(memory_data)

    # Step 4: Execute actions based on response
    logger.info("Executing actions based on response...")
    executor.execute(response)

    # Step 5: Perform additional searches if needed
    logger.info("Performing additional searches if needed...")
    search_results = search_tool.search(response)

    logger.info("Pipeline completed.")
    return search_results

# Example usage
if __name__ == "__main__":
    input_data = "Example input data"
    results = run_pipeline(input_data)
    logger.info(f"Pipeline results: {results}")