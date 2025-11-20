"""
dfs_recursive.py

Recursive Depth-First Search (DFS) implementation for graphs represented
as adjacency lists. Supports two common formats:

1. Simple adjacency dict: node -> list of neighbors
   Example: {'A': ['B','C'], 'B': ['D'], ...}

2. Node dicts with metadata: node -> {'neighbors': [...],
   'visited': ..., 'distance': ...}
   Example: {'A': {'neighbors': ['B','C'], 'visited': False,
   'distance': None}, ...}

The DFSRecursive class performs recursive DFS starting from a given node,
tracking:

- visited nodes
- distances (depth) from the start node
- the DFS traversal path

Optionally, the class updates the internal 'visited' and 'distance' fields
if the nodes are stored as dicts with these keys.
"""

import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualizer:
    """
    Visualizes a graph dictionary using NetworkX and Matplotlib.

    Attributes:
        lst (dict): Graph dictionary with nodes, neighbors, visited status,
        and distance.

    Methods:
        draw(visited_color: str = 'lightgreen',
            unvisited_color: str = 'lightblue'):
            Draws the graph. Visited nodes are colored differently for clarity.
    """

    def __init__(self, lst: dict) -> None:
        self.lst = lst

    def draw(self,
             visited_color: str = 'lightgreen',
             unvisited_color: str = 'lightblue') -> None:
        G = nx.DiGraph()
        colors = []

        for node, data in self.lst.items():
            for neigh in data['neighbors']:
                G.add_edge(node, neigh)

            colors.append(visited_color if data['visited']
                          else unvisited_color)

        pos = nx.spring_layout(G)  # layout algorithm
        nx.draw(
            G, pos,
            with_labels=False,
            node_color=colors,
            arrowsize=20,
            node_size=2000,
            font_size=8
        )

        labels = {
            node: f"{node}\n{data['distance']}" for
            node, data in self.lst.items()}
        nx.draw_networkx_labels(G, pos, labels=labels)

        plt.title("Graph Visualization")
        plt.show()


class DFSRecursive:
    """
    Recursive Depth-First Search (DFS) for a graph.

    Attributes:
        lst (dict): Adjacency list of the graph.
                    Can be either:
                    - node -> list of neighbors
                    - node -> {'neighbors': [...], 'visited': bool,
                    'distance': int}

    Methods:
        run(start_node): Public method to start DFS from 'start_node'.
                        Returns a tuple (distance_dict, traversal_path).
    """

    def __init__(self, lst: dict) -> None:
        self.lst = lst

    def run(self, start_node):
        """
        Start the recursive DFS traversal from a given node.

        Args:
            start_node: Node label to start DFS from.

        Returns:
            tuple:
                distance (dict): Mapping of node -> depth from start_node.
                path (list): List of nodes in the order they were visited.
        """

        visited: set = set()
        distance: dict[str, int] = {}
        path: list[str] = []

        node_data = self.lst.get(start_node)
        if isinstance(node_data, dict) and 'distance' in node_data:
            node_data['distance'] = 0
        distance[start_node] = 0

        self._show(start_node, visited, distance, path, 0)

        return distance, path

    def _show(self, current, visited, distance, path, depth):
        """
        Recursive helper function for DFS traversal.

        Args:
            current: The current node being visited.
            visited (set): Set of already visited nodes.
            distance (dict): Mapping of node -> depth from start node.
            path (list): List of nodes in DFS traversal order.
            depth (int): Depth of the current node from the start node.

        Updates:
            visited, distance, path in place.
            If nodes are stored as dicts with 'visited'/'distance',
            updates them too.
        """

        if current in visited:
            return

        visited.add(current)
        path.append(current)
        distance[current] = depth

        node_data = self.lst.get(current)
        if isinstance(node_data, dict):
            if 'visited' in node_data:
                node_data['visited'] = True
            if 'distance' in node_data:
                node_data['distance'] = depth
            neighbors = node_data.get('neighbors', [])
        else:
            neighbors = node_data if isinstance(node_data, list) else []

        for neighbor in neighbors:
            if neighbor not in visited:
                self._show(neighbor, visited, distance, path, depth + 1)


lst = {
    'A':  {'neighbors': ['B', 'C', 'D', 'F'],
           'distance': None,
           'visited': False},
    'B':  {'neighbors': ['E', 'F', 'H'],
           'distance': None,
           'visited': False},
    'C':  {'neighbors': ['F', 'G'],
           'distance': None,
           'visited': False},
    'D':  {'neighbors': ['H'],
           'distance': None,
           'visited': False},
    'E':  {'neighbors': ['I', 'C'],
           'distance': None,
           'visited': False},
    'F':  {'neighbors': ['D'],
           'distance': None,
           'visited': False},
    'G':  {'neighbors': ['H', 'B'],
           'distance': None,
           'visited': False},
    'H':  {'neighbors': ['C'],
           'distance': None,
           'visited': False},
    'I':  {'neighbors': ['F'],
           'distance': None,
           'visited': False}
}

show_path = DFSRecursive(lst=lst)
distance, path = show_path.run('A')
print(distance)
print(path)
visualizer = GraphVisualizer(lst).draw()
