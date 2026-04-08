# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = deque()
        if root:
            stack.append(root)
        count = 0
        while stack:
            for i in range(len(stack)):                
                lvl_nod = stack.popleft()
                if lvl_nod.left:
                    stack.append(lvl_nod.left)
                if lvl_nod.right:
                    stack.append(lvl_nod.right)
            count += 1

        return count


        