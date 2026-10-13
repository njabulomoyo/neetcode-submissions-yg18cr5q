# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        q = deque()
        q.append([root,1])
        while q:
            for _ in range(len(q)):
                node, lvl = q.popleft()
                res = max(res, lvl)
                if node.left:
                    q.append([node.left,lvl+1])
                if node.right:
                    q.append([node.right,lvl+1])

        return res
                     
            