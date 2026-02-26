import os
from typing import List
from PyPDF2 import PdfReader

class DataLoader:
    """
    A class to handle loading and preprocessing of data.
    """

    def __init__(self, data_directory: str = "E:/Auto_mind_Ai/automind_ai/data"):
        """
        Initialize the DataLoader class.

        Args:
            data_directory (str): Path to the directory containing data files. Defaults to the specified data directory.
        """
        self.data_directory = data_directory

    def list_files(self, extensions: List[str] = None) -> List[str]:
        """
        List all files in the data directory with optional filtering by extensions.

        Args:
            extensions (List[str], optional): List of file extensions to filter by. Defaults to None.

        Returns:
            List[str]: List of file paths.
        """
        try:
            files = []
            for root, _, filenames in os.walk(self.data_directory):
                for filename in filenames:
                    if extensions:
                        if any(filename.endswith(ext) for ext in extensions):
                            files.append(os.path.join(root, filename))
                    else:
                        files.append(os.path.join(root, filename))
            return files
        except Exception as e:
            raise RuntimeError(f"Failed to list files: {e}")

    def load_file(self, file_path: str) -> str:
        """
        Load the content of a file. For PDFs, extract text using PyPDF2.

        Args:
            file_path (str): Path to the file to load.

        Returns:
            str: Content of the file.
        """
        try:
            if file_path.endswith(".pdf"):
                reader = PdfReader(file_path)
                return "\n".join(page.extract_text() for page in reader.pages)
            else:
                with open(file_path, 'r', encoding='utf-8') as file:
                    return file.read()
        except Exception as e:
            raise RuntimeError(f"Failed to load file {file_path}: {e}")

    def load_all_files(self, extensions: List[str] = None) -> List[str]:
        """
        Load the content of all files in the data directory with optional filtering by extensions.

        Args:
            extensions (List[str], optional): List of file extensions to filter by. Defaults to None.

        Returns:
            List[str]: List of file contents.
        """
        try:
            file_paths = self.list_files(extensions)
            return [self.load_file(file_path) for file_path in file_paths]
        except Exception as e:
            raise RuntimeError(f"Failed to load all files: {e}")

if __name__ == "__main__":
    # Example usage
    loader = DataLoader()

    print("Listing all .pdf files...")
    pdf_files = loader.list_files(extensions=[".pdf"])
    print("Found files:", pdf_files)

    print("Loading all .pdf files...")
    for pdf_file in pdf_files:
        print(f"File path: {pdf_file}")