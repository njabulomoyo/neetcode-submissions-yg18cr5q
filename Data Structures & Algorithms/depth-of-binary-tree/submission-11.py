# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        lst = deque()
        if root:
            lst.append(root)
     
        height = 0

        while lst:
            for i in range(len(lst)):
                cut = lst.popleft()
                if cut.left:
                    lst.append(cut.left)
                if cut.right:
                    lst.append(cut.right) 
            height += 1

        return height

         