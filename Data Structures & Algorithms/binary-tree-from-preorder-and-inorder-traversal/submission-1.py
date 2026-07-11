# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    edge case:
        - if neither of the lists are empty: return None

    Solution:
    pre = [1,2,3,4]    [2]
    inorder = [2,1,3,4] [2]

    1st node on pre is the root of the tree
    - in the inorder list, the index of the 1st node splits the list to two part, left and right subtrees
    - then we recurcively work our way through the split lists (the subtrees)
    - continue doing recursion until the end
    - then return the root
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:m+1],inorder[:m])
        node.right = self.buildTree(preorder[m+1:],inorder[m+1:])

        return node
















