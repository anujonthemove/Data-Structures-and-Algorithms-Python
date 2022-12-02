from collections import defaultdict

# To-do:
# 1.
#


class GraphAdjList:
    """
    unweighted graph
    """

    def __init__(self) -> None:
        # dictionary of list
        self.graph = defaultdict(list)

    # In this representation, one needs to manually add the forward and backward node

    def insert_node_directed(self, u, v):
        self.graph[u].append(v)

    # adjacency list representation of graph where we do not have to add the backward node
    def insert_node_undirected(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


# class WeightedGraphAdjList:

#     def __init__(self):
#         self.graph = defaultdict(dict)

#     def insert_weighted_node(self, u, v, w):
#         self.graph[u][v] = w

# weighted adjacencey list representation
class WeightedGraphAdjList:
    def __init__(self):
        # self.num_vertices = num_vertices
        self.graph = []

    def insert_weighted_node(self, u, v, w):
        self.graph.append([u, v, w])


# adjacency matrix representation
class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [
            [0 for column in range(self.num_vertices)]
            for row in range(self.num_vertices)
        ]
