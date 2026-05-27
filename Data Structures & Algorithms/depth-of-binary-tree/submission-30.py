# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = []
        if root:
            s.append([root,1])
        res = 0
        while s:
            node, lvl = s.pop()
            res = max(res,lvl)
            if node.left:
                s.append([node.left,lvl+1])
            if node.right:
                s.append([node.right,lvl+1])
            
        return res
        