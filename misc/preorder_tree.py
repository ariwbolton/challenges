"""Solve the preorder list BST reconstruction problem."""
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

import math

def parse_tree_from_list(L):
    """Parse tree."""
    if len(L) == 0:
        return None

    (root, parsed_until) = parse_tree(
        L=L,
        start=0,
        lower_bound=-math.inf, upper_bound=math.inf
    )

    if parsed_until < len(L):
        return None

    return root


def parse_tree(L=None, start=None, lower_bound=None, upper_bound=None):
    """Returns a 2-tuple. (subtree_root, next_start)

    The subtree constructed starting from "start", where all nodes are between
    "lower_bound" and "upper_bound", and the next index of the list.
    """
    # If we're reached the end, return an empty subtree
    if start == len(L):
        return (Node(None), start)

    if not (lower_bound < L[start] < upper_bound):
        return (Node(None), start)

    # The current node is the subtree root
    subtree_root = Node(L[start])

    # Start at next item
    (left_subtree_root, parsed_until) = parse_tree(
        L=L, start=start + 1,
        lower_bound=lower_bound,
        upper_bound=subtree_root.name
    )

    # Start at item pointed to by end of left subtree parse
    (right_subtree_root, parsed_until) = parse_tree(
        L=L, start=parsed_until,
        lower_bound=subtree_root.name,
        upper_bound=upper_bound
    )

    if left_subtree_root.name is not None or right_subtree_root.name is not None:
        if left_subtree_root.name is None:
            left_subtree_root.name = 'left_{}'.format(subtree_root.name)

        if right_subtree_root.name is None:
            right_subtree_root.name = 'right_{}'.format(subtree_root.name)

        left_subtree_root.parent = subtree_root
        right_subtree_root.parent = subtree_root

    return subtree_root, parsed_until


def render_tree(root):
    """Render tree."""
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    tests = [
        [10, 5, 1, 7, 40, 50],
        [10, 5, 1, 7, 6, 8, 9, 40, 50],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [5, 8, 3, 5, 4],
        []
    ]

    for (i, t) in enumerate(tests):
        root = parse_tree_from_list(t)

        if root is not None:
            print("Rendering tree {}".format(i))
            DotExporter(root).to_picture("root_{}.png".format(i))
            # render_tree(root)
        else:
            print("Invlalid tree {}".format(i))
