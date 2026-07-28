# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Output: list of nodes
    Edge cases: empty tree? return []

    Solution:
    1. traverse the tree using level order traversal.
    2. initiate a queue and a list for results
    3. add all the node.val at the far right of the queue
    4. move to the next level
    5. do this for all levels
    6. return list

    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res













        