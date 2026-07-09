# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Edge case if there is one node: return true
    Solution:
        - traverse thrugh the tree inorder
        - keep track of the previous node valu
        - compare with cur node
        - if its bigger at some point, return false
        - 
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def dfs(node):
            if not node:
                return True
            nonlocal prev

            if not dfs(node.left):
                return False

            if prev >= node.val:
                return False
            prev = node.val
            return dfs(node.right)

        return dfs(root)












        