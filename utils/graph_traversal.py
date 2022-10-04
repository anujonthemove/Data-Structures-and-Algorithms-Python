class GraphTraversal:
    @staticmethod
    def BFS(graph, start_idx):

        queue = []
        visited = [False] * (max(graph) + 1)

        queue.append(start_idx)
        visited[start_idx] = True

        while len(queue) > 0:

            start_idx = queue.pop(0)
            print(start_idx)

            for i in graph[start_idx]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    @staticmethod
    def BFS_disconnected_graph(graph):

        vertices = max((graph)) + 1
        visited = [False] * vertices

        for i in range(vertices):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True

                while len(queue) > 0:

                    index = queue.pop(0)
                    print(index)

                    for idx in graph[index]:
                        if visited[idx] == False:
                            queue.append(idx)
                            visited[idx] = True

    @staticmethod
    def DFS_util(graph, vertex, visited_node_set):

        print(vertex)
        visited_node_set.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited_node_set:
                GraphTraversal.DFS_util(graph, neighbour, visited_node_set)

    @staticmethod
    def DFS(graph, vertex):

        visited_node_set = set()
        GraphTraversal.DFS_util(graph, vertex, visited_node_set)

    @staticmethod
    def DFS_disconnected_graph(graph):

        visited_node_set = set()
        for vertex in graph:
            if vertex not in visited_node_set:
                GraphTraversal.DFS_util(graph, vertex, visited_node_set)
