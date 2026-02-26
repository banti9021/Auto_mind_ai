import requests
from typing import List

class SearchTool:
    """
    A class to perform search operations using external APIs or local data.
    """

    def __init__(self, api_key: str = None):
        """
        Initialize the SearchTool class.

        Args:
            api_key (str, optional): API key for external search services. Defaults to None.
        """
        self.api_key = api_key

    def web_search(self, query: str, num_results: int = 5) -> List[str]:
        """
        Perform a web search using an external API.

        Args:
            query (str): The search query.
            num_results (int, optional): Number of search results to return. Defaults to 5.

        Returns:
            List[str]: A list of search result URLs.
        """
        if not self.api_key:
            raise ValueError("API key is required for web search.")

        try:
            # Example API call (replace with actual search API)
            url = "https://api.example.com/search"
            params = {
                "q": query,
                "num": num_results,
                "key": self.api_key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json()

            # Extract URLs from results (adjust based on actual API response structure)
            return [item["url"] for item in results.get("items", [])]
        except Exception as e:
            raise RuntimeError(f"Failed to perform web search: {e}")

if __name__ == "__main__":
    # Example usage
    api_key = "your_api_key_here"  # Replace with your actual API key
    search_tool = SearchTool(api_key=api_key)

    query = "What is artificial intelligence?"
    print("Performing web search...")
    try:
        results = search_tool.web_search(query)
        print("Search Results:")
        for url in results:
            print(url)
    except Exception as e:
        print(f"Error: {e}")