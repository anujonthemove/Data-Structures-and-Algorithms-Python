# For graph built using adjacency lists
## References
# 1. https://www.geeksforgeeks.org/count-number-edges-undirected-graph/

import operator


class GraphPropertiesAdjList:
    @staticmethod
    def num_vertices(graph):
        return max(graph) + 1

    def num_vertices_updated(graph):
        num_nodes = -1
        for i in graph:
            num_nodes = i
            for j in graph[i]:
                if j > i:
                    num_nodes = j

        return num_nodes + 1

    @staticmethod
    def num_edges(graph):
        count = 0
        for vertex in graph:
            count += len(graph[vertex])
        return count

    @staticmethod
    def print_graph(graph):
        for k, v in graph.items():
            print(f"{k}: {v}")


class WeightedGraphPropertiesAdjList:
    @staticmethod
    def num_vertices_weighted(graph):
        get_nodes = operator.itemgetter(0, 1)
        return max(max(list(map(get_nodes, graph)))) + 1
