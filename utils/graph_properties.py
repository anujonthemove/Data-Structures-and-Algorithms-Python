# For graph built using adjacency lists
## References
# 1. https://www.geeksforgeeks.org/count-number-edges-undirected-graph/


class GraphPropertiesAdjList:
    @staticmethod
    def num_vertices(graph):
        return max(graph) + 1

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
