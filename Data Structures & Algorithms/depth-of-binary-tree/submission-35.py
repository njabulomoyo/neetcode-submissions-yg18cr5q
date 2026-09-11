# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: int - max dept
    edge cases? empty tree? return 0

    solution:
    - we will use recursion
    - base case would be when node is null: return return 0
    - for each node, we compare the left and the right and take max of the two + 1
    - we will work our way up to the root node
    - we return the max depth

    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        