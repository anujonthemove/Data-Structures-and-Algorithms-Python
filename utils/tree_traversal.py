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
