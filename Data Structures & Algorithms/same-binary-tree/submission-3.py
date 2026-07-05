# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Edge case:
    - if only one root exist: return false
    - if both nodes are null: return True
    - 

    Solution:
    Traverse thru both nodes
    first check if the nodes exists
    then check if the numbers inside are the same
    if not equal: return False
    other continue until to all nodes
    Return True
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if q.val != p.val:
            return False
        
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))




