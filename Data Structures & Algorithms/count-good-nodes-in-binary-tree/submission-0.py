# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    edge case?/base case?
    if there is one node, return one

    Solution:
    dfs: inorder traversal
    recursion:
        - have a variable that will keep track of the maximum of the nodes passed so far
        - traverse checking if the  cur nodes are the less than the previous max number
        - count the number of times a number for a node is bigger than the prev max
        - return the count
    """
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(node, p):
            nonlocal count
            if not node:
                return 0         

            if p <= node.val:
                count += 1
            p = max(p,node.val)

            helper(node.left, p)
            helper(node.right,p)

            return count

        return helper(root, root.val)


