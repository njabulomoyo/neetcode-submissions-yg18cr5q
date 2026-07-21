# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    output: root node
    Solution:

    - we want to travers to until we find a null node.
    - for each traversal, check if current node is less or greater than insert node
    - keep track of the prev node on a variable
    - if less, move to the left
    - if greater, move to the right
    - if null, compare prev node:
    - if prev node is greater, then prevnode.left becomes the new node
    - if less, prevNode.right = newNode
    """
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        prevNode = None
        head = root
        while root: #root = null
            prevNode = root #9
            if root.val > val: # 9>6
                root = root.left #root = null
            elif root.val < val:#5<6
                root = root.right 
        node = TreeNode(val)

        if prevNode.val > val: # 9 <6
            prevNode.left = node
        else:
            prevNode.right = node

        return head








