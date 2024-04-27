"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.inorder(root, result)

        return all(result[i - 1] < result[i] for i in range(1, len(result)))

    def inorder(self, root, result):
        if root is None:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)


tr = TreeNode(2)
tr.left = TreeNode(1)
tr.right = TreeNode(3)
s = Solution()
print(s.isValidBST(tr))
