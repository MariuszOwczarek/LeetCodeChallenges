"""
DFS Traversal Module

This module implements a simple DFS (Depth-First Search) traversal
for an unweighted directed graph using a class-based approach.

Features:
- Tracks visited nodes
- Computes distance (depth) from the start node
- Records the exact DFS traversal path
- Prints processing steps and traversal order

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


class DFS:
    """
    Implements Depth-First Search (DFS) on a given graph using a
    stack-based approach.

    Attributes:
        lst (dict): Graph representation where each node maps to a dictionary
                    containing 'neighbors', 'visited', and 'distance'.
        start_node (str): Node where DFS traversal starts (default 'A').
        distance (int): Initial distance for the start node (default 0).
        traversal_path (list): Ordered list of nodes as they are visited.

    Methods:
        show() -> dict:
            Performs DFS traversal starting from `start_node`.
            Marks nodes as visited, computes depth (distance) from start,
            prints each node being processed, and stores the
            DFS traversal order.
            Returns the updated graph dictionary with visited
            status and distances.

    Graph structure example:
        {
            'A': {'neighbors': ['B', 'C'], 'distance': 0, 'visited': False},
            'B': {'neighbors': ['C', 'D'], 'distance': None, 'visited': False},
            'C': {'neighbors': ['D'], 'distance': None, 'visited': False},
            'D': {'neighbors': [], 'distance': None, 'visited': False}
        }
    """

    def __init__(self, lst: dict, start_node='A', distance=0) -> None:
        self.lst = lst
        self.start_node = start_node
        self.distance = distance
        self.traversal_path = []

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
        stack: list = [(current_node, current_distance)]

        while stack:
            item, dist = stack.pop()

            if not self.lst[item]['visited']:
                self.lst[item]['visited'] = True
                self.lst[item]['distance'] = dist
                self.traversal_path.append(item)
                print(f"Processing node: {item}, "
                      f"Distance: {self.lst[item]['distance']}, "
                      f"Neighbors: {self.lst[item]['neighbors']}")

                for neighbor in reversed(self.lst[item]['neighbors']):
                    if not self.lst[neighbor]['visited']:
                        stack.append((neighbor, dist + 1))

        print("\nDFS path with distances:")
        for node in self.traversal_path:
            print(f"{node}({self.lst[node]['distance']})", end=" → ")
        print("END\n")

        return self.lst


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

show_path = DFS(lst=lst, start_node='A', distance=0).show()
visualizer = GraphVisualizer(show_path).draw()
