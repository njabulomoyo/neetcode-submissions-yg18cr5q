# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    output: tree

    edge cases? if root is Null: return TreeNode(val)

    Solution:
    - Traverse thru the tree iteratively
    - keep track root in a variable
    - for each node, check if it is less or greater than Val
    - if less, traverse to left
    - if greater, traverse to right
    - traverse untile you find empty  node: return TreeNode(val)
    - return root
    """
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        prev, head = None, root

        while head:
            prev = head
            if head.val < val:
                head = head.right
            else:
                head = head.left
        node = TreeNode(val)
        if prev.val < node.val:
            prev.right = node
        else:
            prev.left = node

        return root












