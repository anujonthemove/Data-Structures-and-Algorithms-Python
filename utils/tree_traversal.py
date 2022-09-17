from utils.tree_properties import get_height


def print_elements_at_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    else:
        print_elements_at_level(root.left, level - 1)
        print_elements_at_level(root.right, level - 1)


class TreeTraversal:
    @staticmethod
    def traverse_preorder(root):
        """Preorder tree traversal
           Print Root, visit Left, visit Right

        Args:
            root (TreeNode): Root node of a Binary Tree
        """
        if root:
            print(root.data)

        if root.left:
            TreeTraversal.traverse_preorder(root.left)

        if root.right:
            TreeTraversal.traverse_preorder(root.right)

    @staticmethod
    def traverse_inorder(root):
        """Inorder tree traversal
           Visit Left, print Root, visit Right

        Args:
            root (TreeNode): Root node of a Binary Tree
        """

        if root.left:
            TreeTraversal.traverse_inorder(root.left)

        if root:
            print(root.data)

        if root.right:
            TreeTraversal.traverse_inorder(root.right)

    @staticmethod
    def traverse_postorder(root):
        """Postorder tree traversal
           Visit Left, visit Right, print Root

        Args:
            root (TreeNode): Root node of a Binary Tree
        """
        if root.left:
            TreeTraversal.traverse_postorder(root.left)

        if root.right:
            TreeTraversal.traverse_postorder(root.right)

        if root:
            print(root.data)

    @staticmethod
    def print_level_order_traversal_recursive(root):
        height = get_height(root)
        for i in range(1, height + 1):
            print_elements_at_level(root, i)

    @staticmethod
    def level_order_traversal_iterative(root):

        if root is None:
            print("Cannot traverse an empty tree")
            return

        bfs_elements = []
        queue = []

        # insert first element or root into the queue
        queue.append(root)

        while len(queue) > 0:

            # pop the element from the front of the queue
            node = queue.pop(0)
            bfs_elements.append(node.data)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return bfs_elements
