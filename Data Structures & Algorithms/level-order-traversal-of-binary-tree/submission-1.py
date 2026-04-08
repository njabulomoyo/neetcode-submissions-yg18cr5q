# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lst = deque()
        res = []
        
        lst.append(root)
        while lst:
            new = []
            for i in range(len(lst)):
                node = lst.popleft()
                new.append(node.val)
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)
            res.append(new)


        return res

    
        

