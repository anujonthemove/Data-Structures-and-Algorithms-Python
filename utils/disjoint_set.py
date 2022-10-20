class DisjointSetNaive:
    def __init__(self):
        self.parent = {}

    def make_set(self, universe):
        for i in universe:
            self.parent[i] = i

    def find(self, k):
        if self.parent[k] == k:
            return k
        return self.find(self.parent[k])

    def union(self, x, y):

        x_root = self.find(x)
        y_root = self.find(y)

        self.parent[x_root] = y_root

    def print_set(self, universe):
        print([self.find(i) for i in universe])


class DisjointSetOptimized:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, universe):
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, k):
        if self.parent[k] == k:
            return k
        else:
            root = self.find(self.parent[k])
            self.parent[k] = root

    def union(self, x, y):

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
