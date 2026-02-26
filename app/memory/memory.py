class Memory:
    """
    A class to manage memory for storing and retrieving data.
    """

    def __init__(self):
        """
        Initialize the Memory class with an empty storage.
        """
        self.storage = {}

    def store(self, key: str, value: any):
        """
        Store a value in memory with a specific key.

        Args:
            key (str): The key to store the value under.
            value (any): The value to store.
        """
        self.storage[key] = value

    def retrieve(self, key: str) -> any:
        """
        Retrieve a value from memory by its key.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            any: The value stored under the key, or None if the key does not exist.
        """
        return self.storage.get(key, None)

    def delete(self, key: str):
        """
        Delete a value from memory by its key.

        Args:
            key (str): The key of the value to delete.
        """
        if key in self.storage:
            del self.storage[key]

    def clear(self):
        """
        Clear all data from memory.
        """
        self.storage.clear()

if __name__ == "__main__":
    # Example usage
    memory = Memory()

    # Store data
    memory.store("key1", "value1")
    memory.store("key2", 12345)

    # Retrieve data
    print("Key1:", memory.retrieve("key1"))
    print("Key2:", memory.retrieve("key2"))

    # Delete data
    memory.delete("key1")
    print("Key1 after deletion:", memory.retrieve("key1"))

    # Clear memory
    memory.clear()
    print("Memory after clearing:", memory.storage)