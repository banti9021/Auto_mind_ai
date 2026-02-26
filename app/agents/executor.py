from typing import Callable, Dict, Any

class TaskExecutor:
    """
    A class to manage and execute tasks or workflows.
    """

    def __init__(self):
        """
        Initialize the TaskExecutor with an empty task registry.
        """
        self.tasks = {}

    def register_task(self, task_name: str, task_function: Callable):
        """
        Register a task with a name and its corresponding function.

        Args:
            task_name (str): The name of the task.
            task_function (Callable): The function to execute the task.
        """
        self.tasks[task_name] = task_function

    def execute_task(self, task_name: str, **kwargs: Dict[str, Any]) -> Any:
        """
        Execute a registered task by name with the provided arguments.

        Args:
            task_name (str): The name of the task to execute.
            **kwargs (Dict[str, Any]): Arguments to pass to the task function.

        Returns:
            Any: The result of the task execution.
        """
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' is not registered.")

        try:
            return self.tasks[task_name](**kwargs)
        except Exception as e:
            raise RuntimeError(f"Failed to execute task '{task_name}': {e}")

if __name__ == "__main__":
    # Example usage
    executor = TaskExecutor()

    # Define some example tasks
    def add_numbers(a: int, b: int) -> int:
        return a + b

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    # Register tasks
    executor.register_task("add", add_numbers)
    executor.register_task("greet", greet)

    # Execute tasks
    print("Adding numbers:", executor.execute_task("add", a=5, b=3))
    print("Greeting:", executor.execute_task("greet", name="Alice"))