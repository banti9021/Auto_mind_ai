import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "automind_ai"

list_of_files = [

    # App Structure
    f"{project_name}/app/__init__.py",
    f"{project_name}/app/main.py",

    # LLM
    f"{project_name}/app/llm/__init__.py",
    f"{project_name}/app/llm/local_llm.py",

    # RAG
    f"{project_name}/app/rag/__init__.py",
    f"{project_name}/app/rag/loader.py",
    f"{project_name}/app/rag/chunking.py",
    f"{project_name}/app/rag/embeddings.py",
    f"{project_name}/app/rag/vector_store.py",
    f"{project_name}/app/rag/retriever.py",

    # Agents
    f"{project_name}/app/agents/__init__.py",
    f"{project_name}/app/agents/planner.py",
    f"{project_name}/app/agents/executor.py",
    f"{project_name}/app/agents/graph.py",

    # Tools
    f"{project_name}/app/tools/__init__.py",
    f"{project_name}/app/tools/calculator.py",
    f"{project_name}/app/tools/search_tool.py",

    # Memory
    f"{project_name}/app/memory/__init__.py",
    f"{project_name}/app/memory/memory.py",

    # Utils
    f"{project_name}/app/utils/__init__.py",
    f"{project_name}/app/utils/logger.py",

    # Root level
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",

    # Data folders
    f"{project_name}/data/.gitkeep",
    f"{project_name}/embeddings/.gitkeep",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")