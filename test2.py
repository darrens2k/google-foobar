path = [[0, 0, 4, 6, 0, 0], 
        [0, 0, 5, 2, 0, 0], 
        [0, 0, 0, 0, 4, 4], 
        [0, 0, 0, 0, 6, 6], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]]

# path = [[0, 7, 0, 0], 
#         [0, 0, 6, 0], 
#         [0, 0, 0, 8], 
#         [9, 0, 0, 0]]

# entrances = [0]
# exits = [3]
entrances = [0,1]
exits = [4,5]

# first convert the path to a directed weighted graph

# class for nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

# class for edges
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

# class for the directed weighted graph
class DirectedWeightedGraph:
    def __init__(self):
        self.nodes = []
        self.adj_matrix = None
    # function to add nodes
    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
    # function to add edges to nodes
    def add_edge(self, source, destination, weight):
        edge = Edge(source, destination, weight)
        source.edges.append(edge)
    # function to return a node if you know its value (in this case its row/room)
    def get_node_by_value(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    # function to get the index of a node if you know its value
    def get_node_index(self, value):
        node = self.get_node_by_value(value)
        for i in range(len(self.nodes)):
            if self.nodes[i] == node:
                return i
        return None
    # function to create a main input node
    def create_main_input(self, entrance_indices, weight):
        super_input = Node("inputMain")
        # insert main input node at the beginning
        self.nodes.insert(0, super_input)  
        for entrance_index in entrance_indices:
            entrance_node = self.get_node_by_value(entrance_index)
            if entrance_node:
                self.add_edge(super_input, entrance_node, weight)
    # function to create a main exit node
    def create_main_exit(self, exit_indices, weight):
        main_exit = Node("exitMain")
        # append main exit node at the end
        self.nodes.append(main_exit)  
        for exit_index in exit_indices:
            exit_node = self.get_node_by_value(exit_index)
            if exit_node:
                self.add_edge(exit_node, main_exit, weight)
    # function to get the adjacency matrix of the graph
    def get_adjacency_matrix(self):
        num_nodes = len(self.nodes)
        adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        for node in self.nodes:
            source_index = self.get_node_index(node.value)
            for edge in node.edges:
                destination_index = self.get_node_index(edge.destination.value)
                adj_matrix[source_index][destination_index] = edge.weight

        self.adj_matrix = adj_matrix
        
        return adj_matrix
    # function to perform BFS on the graph
    def bfs(self, s, t, parent):
        # s = start node, t = end node, parent = list to store path
        # mark all nodes as not visited
        visited = [False] * len(self.adj_matrix)
 
        # create a queue for BFS
        queue = []
 
        # mark source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # bfs loop
        while queue:
 
            # dequeue a node from queue and print it
            u = queue.pop(0)
 
            # explore all adjacent nodes
            for ind, val in enumerate(self.adj_matrix[u]):
                if visited[ind] == False and val > 0:
                    # end bfs if we reach the end node
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # return false if no valid path exists
        return False
    # returns the maximum flow from s to t in the given graph
    def find_max_flow(self, source, sink):
 
        # path list
        parent = [-1] * len(self.adj_matrix)

        # initialize max flow
        max_flow = 0
        
        # find all possible paths
        while self.bfs(source, sink, parent) :
 
            # find max flow of current pth
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.adj_matrix[parent[s]][s])
                s = parent[s]
 
            # add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            v = sink
            while(v !=  source):
                u = parent[v]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow
                v = parent[v]
 
        return max_flow
        
        
# build graph from path
graph = DirectedWeightedGraph()

# add nodes
for i in range(len(path)):
    graph.add_node(i)

# add edges
for i in range(len(path)):
    for j in range(len(path[i])):
        if path[i][j] != 0:
            source_node = graph.get_node_by_value(i)
            destination_node = graph.get_node_by_value(j)
            # do not add edges from a terminal node, creates cycles
            if source_node and destination_node and i not in exits:
                graph.add_edge(source_node, destination_node, path[i][j])

# create main input if there are more than one entrances
graph.create_main_input(entrances, float('Inf'))
# create main output if there are more than one exits
graph.create_main_exit(exits, float('Inf'))

# build adjancency matrix
graph.get_adjacency_matrix()
print(graph.find_max_flow(0,len(graph.nodes) - 1))


# class FordFulkerson:
#     def __init__(self, graph):
#         self.graph = graph
#     # function to perform a bfs from a source to a target
#     # parent list keeps track of visited nodes
#     def bfs(self, source, target, parent):
#         visited = [False] * len(self.graph.nodes)
#         queue = []
#         queue.append(source)
#         visited[source] = True
#         while len(queue) > 0:
#             u = queue.pop(0)
#             if not visited[u]:
#                 visited[u] = True
#             for edge in self.graph.nodes[u].edges:
#                 v = edge.destination.value
#                 dest_index = self.graph.get_node_index(v)
#                 residual_capacity = edge.weight - edge.flow
#                 if not visited[dest_index] and residual_capacity > 0:
#                     queue.append(dest_index)
#                     parent[dest_index] = u
#                     # visited[dest_index] = True
#         return True if visited[target] else False, parent

#     def ford_fulkerson(self, source, target):
#         parent = [-1] * len(self.graph.nodes)
#         max_flow = 0
        
#         # list to store explored paths
#         explored = []

#         while True:
#             is_path_found, parent = self.bfs(source, target, parent)

#             if not is_path_found or parent in explored:
#                 break
            
#             # add path to explored paths
#             # explored.append(parent)
#             print("looped")
#             path_flow = float("inf")
#             s = target
#             while s != source:
#                 u = parent[s]
#                 for edge in self.graph.nodes[u].edges:
#                     v =  edge.destination.value
#                     if self.graph.get_node_index(v) == s:
#                         path_flow = min(path_flow, edge.weight - edge.flow)
#                         break
#                 s = u

#             # If path_flow is zero, terminate the loop
#             if path_flow == 0:
#                 break
            
#             max_flow += path_flow

#             v = target
#             while v != source:
#                 u = parent[v]
#                 for edge in self.graph.nodes[u].edges:
#                     if edge.destination.value == v:
#                         edge.flow += path_flow
#                         break
#                 for back_edge in self.graph.nodes[v].edges:
#                     if back_edge.destination.value == u:
#                         back_edge.flow -= path_flow
#                         break
#                 v = u

#             parent = [-1] * len(self.graph.nodes)

#         return max_flow

# # Run Ford-Fulkerson algorithm on the graph
# ff = FordFulkerson(graph)
# source = 0  # Index of the source node (inputMain)
# target = len(graph.nodes) - 1  # Index of the target node (exitMain)
# max_flow = ff.ford_fulkerson(source, target)
# print("Maximum flow of the graph:", max_flow)

