# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        count = 0
        if root:
            stack.append([root,-101])

        while stack:
            node, prevG = stack.pop()
            if node.val >= prevG:
                count += 1
            prevG = max(prevG, node.val)
            if node.left:
                stack.append([node.left,prevG])
            if node.right:
                stack.append([node.right, prevG])
        
        return count





