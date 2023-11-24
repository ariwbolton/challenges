"""Testing Dijkstras Algo."""
import heapq
import math


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edge_values = dict()
        self.edges = dict()

    @staticmethod
    def from_edges(edges):
        new_graph = Graph()

        for (n1, n2, v) in edges:
            new_graph.add_node(n1)
            new_graph.add_node(n2)

            edge_key = Graph._edge_key(n1, n2)

            if edge_key not in new_graph.edges:
                new_graph.add_edge(n1, n2, v)

        return new_graph

    def add_node(self, n):
        self.nodes.add(n)

    def add_edge(self, n1, n2, v):
        edge_key = self._edge_key(n1, n2)

        if edge_key in self.edge_values:
            raise ValueError("Edge {} already exists".format(edge_key))

        self.edge_values[edge_key] = v

        if n1 not in self.edges:
            self.edges[n1] = set()

        self.edges[n1].add(n2)

        if n2 not in self.edges:
            self.edges[n2] = set()

        self.edges[n2].add(n1)

    def get_edge_weight(self, n1, n2):
        edge_key = self._edge_key(n1, n2)

        if edge_key not in self.edge_values:
            raise ValueError("Edge {} doesn't exist".format(edge_key))

        return self.edge_values[edge_key]

    def get_edges(self, n1):
        return self.edges[n1]

    def has_edge(self, n1, n2):
        return n2 in self.edges[n1]

    @staticmethod
    def _edge_key(n1, n2):
        return (n2, n1) if n1 > n2 else (n1, n2)

def dijkstras(g, initial):
    """Attempt to use heapq to run Dijkstras."""
    heap_list = list()
    node_heap_map = dict()

    unvisited = set(g.nodes)
    prev = {n: None for n in g.nodes}

    for n in g.nodes:
        if n == initial:
            initial_dist = 0
        else:
            initial_dist = math.inf

        initial_values = [initial_dist, n]

        heapq.heappush(heap_list, initial_values)
        node_heap_map[n] = initial_values

    while len(heap_list) > 0:
        node_values = heapq.heappop(heap_list)

        current_dist = node_values[0]
        this_node = node_values[1]

        unvisited.remove(this_node)

        for neighbor in g.get_edges(this_node):
            if neighbor not in unvisited:
                continue

            neighbor_values = node_heap_map[neighbor]
            current_neighbor_dist = neighbor_values[0]

            edge_weight = g.get_edge_weight(this_node, neighbor)

            if current_neighbor_dist > current_dist + edge_weight:
                neighbor_values[0] = -1

                new_neighbor_values = [current_dist + edge_weight, neighbor]

                node_heap_map[neighbor] = new_neighbor_values
                heapq.heappush(heap_list, new_neighbor_values)

                prev[neighbor] = this_node

        # Remove invalid node values from heap
        while len(heap_list) > 0 and heap_list[0][0] == -1:
            heapq.heappop(heap_list)

    distances_map = {n: v[0] for (n, v) in node_heap_map.items()}

    return distances_map, prev


def print_info(distances, prev):
    for node, distance in sorted(list(distances.items()), key=lambda x: x[1]):
        print("{}: {} <- {}".format(node, distance, prev[node]))

if __name__ == '__main__':
    tests = [
        [
            (1, 3, 5),
            (1, 2, 1),
            (2, 3, 3),
            (4, 5, 1)
        ]
    ]

    for t in tests:
        distances, prev = dijkstras(Graph.from_edges(t), 1)

        print_info(distances, prev)

