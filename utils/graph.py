from collections import defaultdict


class GraphAdjList:
    def __init__(self) -> None:
        # dictionary of list
        self.graph = defaultdict(list)

    def insert_node(self, vertex, data):
        self.graph[vertex].append(data)
