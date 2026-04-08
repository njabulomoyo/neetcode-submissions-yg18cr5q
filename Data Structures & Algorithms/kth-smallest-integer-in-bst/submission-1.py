# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        res = None
        cnt = 0

        def inOrder(node):
            nonlocal cnt, res, k
            if node:
                inOrder(node.left)
                cnt += 1
                if cnt == k:
                    res = node.val
                    return
                inOrder(node.right)
            

        inOrder(root)

        return res
        

        