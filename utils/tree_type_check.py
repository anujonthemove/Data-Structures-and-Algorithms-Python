class TreeTypeCheck:
    @staticmethod
    def is_full_tree(root):
        """Check if a given tree is a full or perfect binary tree or not
        Logic:
        A full tree condition is satisfied for the following cases:
        1. Node is empty
        2. Both left and right of Node are empty
        3. If left and right of a Node are not empty then check
        all these conditions for the subtrees and these should hold
        true for both left and right subtree

        Args:
            root (Node): Tree

        Returns:
            bool: True if tree is a Full or Perfect Binary Tree; False otherwise
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.right is not None:
            return (TreeTypeCheck.is_full_tree(root.left)) and (
                TreeTypeCheck.is_full_tree(root.right)
            )

        return False

    @staticmethod
    def is_perfect_using_depth(root, depth, level=0):
        if root is None:
            return True

        # this condition must be checked first otherwise it returns false
        # which is vague
        # and
        if root.left is None and root.right is None:
            return depth == level + 1

        # or - if either of the nodes is none then condition is violated
        if root.left is None or root.right is None:
            return False

        return TreeTypeCheck.is_perfect_using_depth(
            root.left, depth, level + 1
        ) and TreeTypeCheck.is_perfect_using_depth(root.right, depth, level + 1)

    @staticmethod
    def is_perfect_using_node_count(root):
        count = count_nodes(root)
        return count and (not (count & (count - 1)))
        return (count & count + 1) == 0

    @staticmethod
    def is_complete(root, index, num_nodes):
        """A complete binary tree has a property:
        left child of node at index i can be found at: 2*i+1 index
        right child of node at index i can be found at: 2*i+2 index

        Args:
            root (_type_): tree root
            index (_type_): starting index(0)
            num_nodes (_type_): count of total number of nodes

        Returns:
            bool: True if tree is a complete binary tree False otherwise
        """

        if root is None:
            return True

        if index >= num_nodes:
            return False

        return TreeTypeCheck.is_complete(
            root.left, 2 * index + 1, num_nodes
        ) and TreeTypeCheck.is_complete(root.right, 2 * index + 2, num_nodes)


def calculate_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.left
    return depth


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
