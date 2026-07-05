# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Binary search tree
    output: int
    recursion, traverse thru the tree

    if p a node or  int

    Solution:
     - traverse (inorder) thru the tree
     - for each node check if the value is in between q and p
     - if not continue, check nxt node
     - continue until you find the LCA
     - base case, 
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:      
        
        if root.val < p.val and root.val < q.val :
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root
            
        
        