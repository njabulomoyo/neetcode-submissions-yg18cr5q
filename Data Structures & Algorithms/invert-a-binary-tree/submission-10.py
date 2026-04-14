# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output - binary tree

    solution:
    - iterate thru each node
    - for each node, swap the left child and the right child 's positions
    - left child will be right, right child will be left
    - do this for every node on the tree
    - return root node
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        left = root.left
        root.left = root.right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root





