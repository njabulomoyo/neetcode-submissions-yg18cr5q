# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Edge case:
        - if the there one node: return 1

    Solution:
    Recursive nature
    initiate a count variable
    traverse through the tree
    check if the current tree is equal or bigger than the maxValue of node on the path
    if true, add one to the count variable
    else, move to nxt node
    do thid for all nodes
    return count var
    """
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,maxVal):
            if not node:
                return 0

            nonlocal count

            if node.val >= maxVal:
                count += 1

            maxVal = max(node.val, maxVal)

            dfs(node.left,maxVal)
            dfs(node.right, maxVal)

            return count

        return dfs(root, root.val)










        