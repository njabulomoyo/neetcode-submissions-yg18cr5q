# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node,isBalanced):
            if not node:
                return [0,True]

            left = helper(node.left, isBalanced)
            right = helper(node.right, isBalanced)

            isBalanced = (abs(left[0]-right[0]) <= 1) and left[1] and right[1]

            return [1 + max(left[0],right[0]), isBalanced]
        
        res = helper(root, True)

        return res[1]

            

