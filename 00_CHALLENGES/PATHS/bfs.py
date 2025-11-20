"""
BFS Traversal Module

This module implements a simple BFS (Breadth-First Search) traversal
for an unweighted directed graph using a class-based approach.

Features:
- Tracks visited nodes
- Computes distance (number of steps) from the start node
- Prints final graph state with neighbors, visited status, and distances

The graph is represented as a dictionary where each key is a node,
and each value is another dictionary containing:
    - 'neighbors': list of neighboring nodes
    - 'visited': boolean, True if the node has been visited
    - 'distance': number of steps from the start node (None if unvisited)
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


class BFS:
    """
    Implements Breadth-First Search (BFS) on a given graph.

    Attributes:
        lst (dict): Graph representation where each node maps to a dictionary
                    containing 'neighbors', 'visited', and 'distance'.

    Methods:
        show() -> dict:
            Performs BFS traversal starting from node 'A'.
            Marks nodes as visited, computes distances (steps from 'A'),
            and prints the final state of the graph.

    Graph structure example:
        {
            'A': {'neighbors': ['B', 'C'], 'distance': 0, 'visited': False},
            'B': {'neighbors': ['C', 'D'], 'distance': None, 'visited': False},
            'C': {'neighbors': ['D'], 'distance': None, 'visited': False},
            'D': {'neighbors': [], 'distance': None, 'visited': False}
        }
    """

    def __init__(
        self,
        lst: dict,
        start_node: str = 'A',
        distance: int = 0
    ) -> None:
        self.lst = lst
        self.start_node = start_node
        self.distance = distance

    def show(self) -> dict:
        if self.start_node not in self.lst:
            raise ValueError(f"start_node {self.start_node!r}"
                             f" is not in the graph")

        for node in self.lst:
            self.lst[node]['visited'] = False
            self.lst[node]['distance'] = None

        current_node: str = self.start_node
        current_distance: int = self.distance
        self.lst[current_node]['distance'] = int(current_distance)
        queue_list: list[str] = [current_node]

        while queue_list:
            item: str = queue_list.pop(0)
            self.lst[item]['visited'] = True

            for neighbor in self.lst[item]['neighbors']:
                if not self.lst[neighbor]['visited']:
                    self.lst[neighbor]['visited'] = True
                    current_distance: int = self.lst[item]['distance']
                    self.lst[neighbor]['distance'] = current_distance + 1
                    queue_list.append(neighbor)

        print("Final graph state:")
        for node in self.lst:
            neighbors: list[str] = self.lst[node]['neighbors']
            neighbors_str: str = ', '.join(neighbors) if neighbors else "None"
            visited: bool = self.lst[node]['visited']
            distance: int | None = self.lst[node]['distance']
            info: str = (
                f"Node {node}, visited:{visited}, "
                f"distance:{distance} ->"
            )
            print(info, "neighbors:", neighbors_str)
        return self.lst


lst = {
    'A': {'neighbors': ['B', 'C'], 'distance': None, 'visited': False},
    'B': {'neighbors': ['D', 'E'], 'distance': None, 'visited': False},
    'C': {'neighbors': ['F'], 'distance': None, 'visited': False},
    'D': {'neighbors': ['G'], 'distance': None, 'visited': False},
    'E': {'neighbors': ['G', 'H'], 'distance': None, 'visited': False},
    'F': {'neighbors': ['H'], 'distance': None, 'visited': False},
    'G': {'neighbors': ['I'], 'distance': None, 'visited': False},
    'H': {'neighbors': ['I'], 'distance': None, 'visited': False},
    'I': {'neighbors': ['J'], 'distance': None, 'visited': False},
    'J': {'neighbors': [], 'distance': None, 'visited': False}
}
show_path = BFS(lst=lst, start_node='A').show()
visualizer = GraphVisualizer(show_path).draw()
