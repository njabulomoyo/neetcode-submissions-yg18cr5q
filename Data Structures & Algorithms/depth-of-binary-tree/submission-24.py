# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output - int

    solution:
    - using level order traversal
    1. initiate queue used for each level
    1.5 initiate count variable for counting the number of levels passed
    2. for each node on level, add child nodes to the back of queue
    3. iterate thru all the nodes
    4. return count variable  
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
                







        