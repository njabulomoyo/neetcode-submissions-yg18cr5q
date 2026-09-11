# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: bool
    edge cases? empty tree? no empty tree

    brainstorm:
    need to visit every node
    we can use inorder travesal
    check if the prev node is less than the curr node
    if not return False
    else continue
    use a recursive solution
    base case is null node: return True


    solution:
    - use resursion
    - use inorder traveral to go thru the tree
    - store the val of the prev node
    - compare with cur node, 
    - if less than return 
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower, upper):
            if not node:
                return True

            

            if not (lower < node.val < upper):
                return False


            return (dfs(node.right, node.val, upper) and
                dfs(node.left, lower, node.val))

        

        return dfs(root, float("-inf"), float("inf"))
    
     









        