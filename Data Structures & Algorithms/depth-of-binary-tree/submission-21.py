# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        d = deque()
        if root:
            d.append([root,1])
        level = 0

        while d:
            for _ in range(len(d)):
                node, depth = d.popleft()
                if node:
                    level = max(level, depth)
                    d.append([node.left,depth + 1])
                    d.append([node.right, depth + 1])

        return level
            
                
















