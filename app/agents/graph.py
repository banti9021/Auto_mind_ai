import networkx as nx
from typing import Any, Dict, List, Tuple

class GraphManager:
    """
    A class to manage and process graph structures.
    """

    def __init__(self):
        """
        Initialize the GraphManager with an empty directed graph.
        """
        self.graph = nx.DiGraph()

    def add_node(self, node_id: Any, **attributes: Dict[str, Any]):
        """
        Add a node to the graph.

        Args:
            node_id (Any): The unique identifier for the node.
            **attributes (Dict[str, Any]): Additional attributes for the node.
        """
        self.graph.add_node(node_id, **attributes)

    def add_edge(self, source: Any, target: Any, **attributes: Dict[str, Any]):
        """
        Add a directed edge to the graph.

        Args:
            source (Any): The source node identifier.
            target (Any): The target node identifier.
            **attributes (Dict[str, Any]): Additional attributes for the edge.
        """
        self.graph.add_edge(source, target, **attributes)

    def get_neighbors(self, node_id: Any) -> List[Any]:
        """
        Get the neighbors of a node.

        Args:
            node_id (Any): The node identifier.

        Returns:
            List[Any]: A list of neighboring nodes.
        """
        return list(self.graph.successors(node_id))

    def shortest_path(self, source: Any, target: Any) -> List[Any]:
        """
        Find the shortest path between two nodes.

        Args:
            source (Any): The source node identifier.
            target (Any): The target node identifier.

        Returns:
            List[Any]: A list of nodes representing the shortest path.
        """
        try:
            return nx.shortest_path(self.graph, source=source, target=target)
        except nx.NetworkXNoPath:
            raise ValueError(f"No path exists between {source} and {target}.")

if __name__ == "__main__":
    # Example usage
    graph_manager = GraphManager()

    # Add nodes
    graph_manager.add_node("A", label="Start")
    graph_manager.add_node("B", label="Middle")
    graph_manager.add_node("C", label="End")

    # Add edges
    graph_manager.add_edge("A", "B", weight=1)
    graph_manager.add_edge("B", "C", weight=2)

    # Get neighbors
    print("Neighbors of B:", graph_manager.get_neighbors("B"))

    # Find shortest path
    print("Shortest path from A to C:", graph_manager.shortest_path("A", "C"))