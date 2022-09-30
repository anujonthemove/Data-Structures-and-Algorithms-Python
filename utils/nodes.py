# References
# 1. https://www.geeksforgeeks.org/python-access-parent-class-attribute/


class BinaryTreeNode(object):
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return "<Node: %s>" % self.data


class AVLTreeNode(BinaryTreeNode):
    def __init__(self, data) -> None:
        self.height = 1
        BinaryTreeNode.__init__(self, data)


class BTreeNode(object):
    def __init__(self, leaf=False) -> None:
        self.leaf = leaf
        self.keys = []
        self.child = []
