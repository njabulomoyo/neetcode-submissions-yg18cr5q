# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output - bool
    edge cases: if root is empty: return None

    Solution:
    - travers thru the whole tree
    - for each node, calculate max height of left & right
    - check if the difference is not more than 1
    - if more, return False
    - if not continue
    - return bool



    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = (left[0] and right[0] and (abs(left[1] - right[1]) < 2))

            return [balanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]

        










        