# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Solution:
        - use recursive function
        - for each node, add height of left and right side
        - height of each side is max of left and right 
        - base case - when node is none, return zero
        - iterate recursively through the tree
        - have a nonlocal variable to keep count of max diameter on each recursive call
        - return diameter
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(node):
            nonlocal res

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        helper(root)
        return res








