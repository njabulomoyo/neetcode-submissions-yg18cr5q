# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Output: int - number of good nodes
    solution:
    do we need to traverse thru all the nodes? yes
    recursion is applicable.
    - initiate counter variable
    - initiate a var to keep track of the current greatest value alog a path
    - for each node traversed, check if >= curr greatest, add to counter
    - otherwise continue
    - traverse thru the whole tree
    - return count var
    """
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, prevG):
            nonlocal count
            if not node:
                return 0
            if node.val >= prevG:
                count += 1
                prevG = node.val

            dfs(node.left,prevG)
            dfs(node.right,prevG)

            return count
        dfs(root, -102)
        return count








        