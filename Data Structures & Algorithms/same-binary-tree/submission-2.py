# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(nodeA,nodeB):
            if not nodeA and not nodeB:
                return True
            if not (nodeA and nodeB):
                return False
            
            if nodeA.val != nodeB.val:
                return False
            return (helper(nodeA.left,nodeB.left) and
            helper(nodeA.right,nodeB.right))

        return helper(p,q)

