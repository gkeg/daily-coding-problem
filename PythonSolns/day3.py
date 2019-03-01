"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

Let the marker for NULL pointer just be #
"""

NULL = "#"


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Simple preorder traversal serialization
# Add to our result as we go along
def serialize_helper(root, res):
    # Print root if null
    if (root is None):
        res += NULL
        return

    # Otherwise, recurse on the children
    res[0] += str(root.val) + " "
    serialize_helper(root.left, res)
    serialize_helper(root.right, res)


# Using a pretty hacky way to pass a primitive by reference in python
def serialize(root):
    res = [""]
    serialize_helper(root, res)
    return res[0]


# Idea is that we do the same pre-order recursive calls on deserialize
def deserialize_helper(str_arr, cur_ind):
    # If we've reached null or
    if cur_ind[0] >= len(str_arr) or str_arr[cur_ind[0]] == NULL:
        return

    # Deserialize time, make the root and append to the left/right
    root = TreeNode(str_arr[cur_ind[0]])
    cur_ind[0] += 1
    root.left = deserialize_helper(str_arr, cur_ind)
    cur_ind[0] += 1
    root.right = deserialize_helper(str_arr, cur_ind)
    return root


def preorder(root):
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


# Helper so that cur_ind gets updated as we go along
def deserialize(string):
    cur_ind = [0]
    str_arr = string.split()
    root = deserialize_helper(str_arr, cur_ind)
    return root


if __name__ == "__main__":
    node = TreeNode('root',
                    TreeNode('left', TreeNode('left.left')),
                    TreeNode('right'))

    # Expected: 'left.left'
    res = serialize(node)
    print(res)
    node = deserialize(res)
    print(deserialize(serialize(node)).left.left.val)

