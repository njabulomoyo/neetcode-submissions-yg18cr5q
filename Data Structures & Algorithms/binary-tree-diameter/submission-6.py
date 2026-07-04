# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    - For each node, you check the left and right side to compare the max
    - max length at each side would be 1 + max(left and right)
    - at each node, add left and right, compare with curr max
    - then return the maximum diameter
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            self.d = max(self.d, left + right)

            return 1 + max(left, right)
        helper(root)
        return self.d

        





