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


def get_height(root):

    # if tree is empty
    # or you have reached a leaf node
    if root is None:
        return 0

    # since there is no way to know in advance
    # which sub tree is going be deeper
    # so we calculate the height of both
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    # now whichever subtree has more height
    # we return that
    # + 1 is done so as to increment the count from 0
    # because at the end when we reach the leaf node
    # we return 0
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1
