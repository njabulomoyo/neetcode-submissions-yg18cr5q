# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    edge case:
        - if not root: return 
        - initialize empty list
        - traverse thru tree using level order traversal
        - for each node at each level, add to the result list
        - return result list
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            new = []
            for _ in range(len(q)):
                node = q.popleft()
                new.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(new)

        return res