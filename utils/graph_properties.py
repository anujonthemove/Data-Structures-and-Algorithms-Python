# For graph built using adjacency lists


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
