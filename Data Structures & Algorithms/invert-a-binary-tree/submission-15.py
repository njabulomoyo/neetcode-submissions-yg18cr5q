# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    outout: inverted tree
    edge cases? empty tree? return empty []

    solution:
     - iterate thru every node (recursively)
     - for each node, we swap the child nodes
     - we go thru all the nodes
     - we return the inverted tree

    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        