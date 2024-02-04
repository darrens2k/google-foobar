class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []  # List to store outgoing edges

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class DirectedWeightedGraph:
    def __init__(self):
        self.nodes = []
        self.entrances = set()  # Set to store indices of source nodes
        self.exits = set()  # Set to store indices of target nodes

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)

    def add_edge(self, source, destination, weight):
        edge = Edge(source, destination, weight)
        source.edges.append(edge)

    def get_node_by_value(self, value):
        """Returns the node with the given value if it exists in the graph."""
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def add_entrance(self, index):
        self.entrances.add(index)

    def add_exit(self, index):
        self.exits.add(index)

    def is_entrance(self, index):
        return index in self.entrances

    def is_exit(self, index):
        return index in self.exits


def ford_fulkerson(graph, source_indices, target_indices):
    max_flow = 0

    # Initialize residual graph with the same structure as the original graph
    residual_graph = DirectedWeightedGraph()
    for node in graph.nodes:
        residual_graph.add_node(node.value)

    # Copy edges from original graph to residual graph
    for node in graph.nodes:
        for edge in node.edges:
            residual_graph.add_edge(edge.source, edge.destination, edge.weight)

    while True:
        # Use Breadth-First Search to find augmenting path
        path, min_capacity = bfs(residual_graph, source_indices, target_indices)
        if min_capacity == 0:
            break  # If no augmenting path is found, break out of the loop

        max_flow += min_capacity

        # Update residual capacities of edges along the augmenting path
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            for edge in residual_graph.get_node_by_value(u).edges:
                if edge.destination.value == v:
                    edge.weight -= min_capacity
                    break
            # Add reverse edge with capacity equal to the flow sent
            for edge in residual_graph.get_node_by_value(v).edges:
                if edge.destination.value == u:
                    edge.weight += min_capacity
                    break

    return max_flow

def bfs(graph, source_indices, target_indices):
    visited = set()
    queue = []
    parent = {}
    min_capacity = float('inf')

    for source in source_indices:
        queue.append(source)
        visited.add(source)

    while queue:
        u = queue.pop(0)
        for edge in graph.get_node_by_value(u).edges:
            v = edge.destination.value
            if edge.weight > 0 and v not in visited:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                min_capacity = min(min_capacity, edge.weight)

    # Reconstruct path and find minimum capacity
    path = []
    v = target_indices.pop()  # Take one of the target nodes
    while v in parent:
        path.insert(0, v)
        v = parent[v]
    path.insert(0, v)

    return path, min_capacity

# Example usage:
path = [[0, 7, 0, 0], 
        [0, 0, 6, 0], 
        [0, 0, 0, 8], 
        [9, 0, 0, 0]]

graph = DirectedWeightedGraph()

# Add nodes
for i in range(len(path)):
    graph.add_node(i)

# Add edges
for i in range(len(path)):
    for j in range(len(path[i])):
        if path[i][j] != 0:
            graph.add_edge(graph.get_node_by_value(i), graph.get_node_by_value(j), path[i][j])

# Define source and target nodes
entrances = [0]  # Example source nodes
exits = [2]  # Example target nodes

# Add source and target nodes to the graph
for entrance in entrances:
    graph.add_entrance(entrance)
for exit in exits:
    graph.add_exit(exit)

# Calculate max flow
max_flow = ford_fulkerson(graph, entrances, exits)
print("Max Flow:", max_flow)
