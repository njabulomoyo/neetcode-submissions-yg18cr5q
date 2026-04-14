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
    1. initiate queue
    2. if the root exist, add array wth root and counter (for number of levels/depth) to queue
    3. iterate len(queue) times to capture node at each level
    4. append child nodes of each child if the exist
    5. add one to counter for next level
    6. iterate through all the nodes
    7. return the counter
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        
        res = 0
        while stack:
            node, count = stack.pop()

            if node:
                res = max(res,count)
                stack.append([node.left, count+1])
                stack.append([node.right, count+1])
                
        return res

                

        
        
        
                







        