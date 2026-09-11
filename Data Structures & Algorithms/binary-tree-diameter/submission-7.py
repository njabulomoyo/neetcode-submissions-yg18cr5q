# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: int max diameter

    edge cases? no empty tree

    solution:
    - we will check the left and the right 
    - len of each node will be max of left and right + 1
    - for ech node, we check the max dia by adding left and right then comparing with max so far
    - keep track of the max diametre
    - do this recursively, base case being empty node: return 0
    - return the max diameter

    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node):
            if not node:
                return 0

            nonlocal d
            left = dfs(node.left)
            right = dfs(node.right)

            d = max(d, left + right)

            return 1 + max(left, right)

        dfs(root)
        return d
            











        