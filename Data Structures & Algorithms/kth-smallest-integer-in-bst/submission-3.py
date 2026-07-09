# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output = int
    edge cases:
    k cannt be > number of nodes on tree
    if not node: return 0
    solution:
        - traverse in order
        - have a counter to track the kth value
        - once count == k: return the value of node
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None
        def dfs(node):
            if not node:
                return 0

            nonlocal count, res
            
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            
            dfs(node.right)
        dfs(root)
        return res

       

        









        