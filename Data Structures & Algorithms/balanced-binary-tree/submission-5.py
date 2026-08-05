# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: Boolean
    edge cases: empty tree? True
    Solution:
    - traverse recursively trhu all the node
    - for each node, check if tree is balanced by comparing the left and right side
    - also make sure that you check if the prvious subtrees wer balance
    - if they were you proceed to check the left and right
    - if not return false
    -Traverse till the end
    - return True

    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left[0] - right[0]) > 1:
                return [-1, False]

            isBalanced = (left[1] and right[1])

            return [1 + max(left[0],right[0]), isBalanced]

        res = dfs(root)

        return res[1]

            

            







        