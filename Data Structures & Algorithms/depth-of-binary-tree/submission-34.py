# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    - initiate stack
    - push the node with its lvl to the stack (as a list)
    pop the stack,
    - check if node has child nodes, if true add the child nodes back to
    the stack with the levels updated
    - iterate until the stack has one element left
    - return lvl

    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append([root,1])
        height = 0
        while stack:
            node, lvl = stack.pop()
            if node.left:
                stack.append([node.left,lvl+1])
            if node.right:
                stack.append([node.right,lvl+1])
            
            height = max(height,lvl)

        return height

        






