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


def get_height_concise(root):

    if root is None:
        return 0

    return max(get_height_concise(root.left), get_height_concise(root.right)) + 1


def is_balanced_naive(root):
    if root is None:
        return True

    # calculate the height of both
    # left subtree and right subtree of the current node
    left_height = get_height_concise(root.left)
    right_height = get_height_concise(root.right)

    # check if the difference between left height and right height
    # is less than or equal to 1.
    # and then recursively check for left and right subtree
    if (
        (abs(left_height - right_height) <= 1)
        and is_balanced_naive(root.left)
        and is_balanced_naive(root.right)
    ):
        return True
    return False


def is_balanced_optimized(root):
    # while calculating height only we check
    # whether the tree is balanced or not
    if root is None:
        return True

    left_height = is_balanced_optimized(root.left)

    if left_height == -1:
        return -1

    right_height = is_balanced_optimized(root.right)

    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced_optimized_driver(root):
    check_height = is_balanced_optimized(root)
    if check_height == -1:
        print("Tree is not balanced")
    else:
        print("Tree is balanced with height: {}".format(check_height))
