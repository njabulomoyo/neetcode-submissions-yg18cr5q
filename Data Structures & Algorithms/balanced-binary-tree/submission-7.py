# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: bool 
    edge cases? if root is null: return True

    Brainstorm:
    - check every node, subtree, to see if there is balance
    - might use recursion over iteration
    - find the left and right lengths
    - find a way to check for the balance at each node

    solution
    - recursion to go thru all the elems on the tree
    - base case empty node: return true
    - find the length of the left and right 
    - 1 + max(left and right)
    - make sure that if a check returns false, the whole thing becomes false, even after finding other true subtrees
    - 
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            
            balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2


            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        


















        