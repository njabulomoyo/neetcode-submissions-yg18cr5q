# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    - recursive
    - length of the left and right side
    - each side would be 1 + max(left and right side)
    - max diameter would be left + right
    - traverse through the nodes 
    - return max diameter

    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def helper(node):
            if not node:
                return 0
            nonlocal d
            
            left = helper(node.left)
            right = helper(node.right)

            d = max(d,left+right)

            return 1 + max(left,right)
        helper(root)
        return d









        