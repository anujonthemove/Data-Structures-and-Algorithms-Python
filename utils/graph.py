from collections import defaultdict


class GraphAdjList:
    """
    unweighted graph
    """

    def __init__(self) -> None:
        # dictionary of list
        self.graph = defaultdict(list)

    # In this representation, one needs to manually add the forward and backward node

    def insert_node(self, u, v):
        self.graph[u].append(v)

    def insert_node_bothways(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


# class WeightedGraphAdjList:

#     def __init__(self):
#         self.graph = defaultdict(dict)

#     def insert_weighted_node(self, u, v, w):
#         self.graph[u][v] = w


class WeightedGraphAdjList:
    def __init__(self):
        # self.num_vertices = num_vertices
        self.graph = []

    def insert_weighted_node(self, u, v, w):
        self.graph.append([u, v, w])
