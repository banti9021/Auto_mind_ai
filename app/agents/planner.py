from typing import List, Dict, Any
from .executor import TaskExecutor
from .graph import GraphManager

class TaskPlanner:
    """
    A class to plan and manage task workflows.
    """

    def __init__(self, executor: TaskExecutor, graph_manager: GraphManager):
        """
        Initialize the TaskPlanner with an executor and a graph manager.

        Args:
            executor (TaskExecutor): The task executor to execute tasks.
            graph_manager (GraphManager): The graph manager to manage task dependencies.
        """
        self.executor = executor
        self.graph_manager = graph_manager

    def add_task(self, task_name: str, dependencies: List[str] = None, **attributes: Dict[str, Any]):
        """
        Add a task to the workflow graph.

        Args:
            task_name (str): The name of the task.
            dependencies (List[str], optional): List of task names this task depends on. Defaults to None.
            **attributes (Dict[str, Any]): Additional attributes for the task.
        """
        self.graph_manager.add_node(task_name, **attributes)
        if dependencies:
            for dependency in dependencies:
                self.graph_manager.add_edge(dependency, task_name)

    def execute_plan(self):
        """
        Execute the planned tasks in the order of their dependencies.
        """
        try:
            # Get the topological order of tasks
            task_order = list(self.graph_manager.graph)
            for task_name in task_order:
                print(f"Executing task: {task_name}")
                self.executor.execute_task(task_name)
        except Exception as e:
            raise RuntimeError(f"Failed to execute plan: {e}")

if __name__ == "__main__":
    # Example usage
    executor = TaskExecutor()
    graph_manager = GraphManager()
    planner = TaskPlanner(executor, graph_manager)

    # Define some example tasks
    def task_a():
        print("Task A executed.")

    def task_b():
        print("Task B executed.")

    def task_c():
        print("Task C executed.")

    # Register tasks
    executor.register_task("TaskA", task_a)
    executor.register_task("TaskB", task_b)
    executor.register_task("TaskC", task_c)

    # Add tasks to the planner with dependencies
    planner.add_task("TaskA")
    planner.add_task("TaskB", dependencies=["TaskA"])
    planner.add_task("TaskC", dependencies=["TaskB"])

    # Execute the plan
    planner.execute_plan()