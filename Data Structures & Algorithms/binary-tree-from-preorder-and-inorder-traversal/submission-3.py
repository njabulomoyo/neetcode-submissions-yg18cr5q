# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    output: list
    edge cases: in one of the lists is empty: return []

    solution:
    - start with the preOrder, first number is the root
    - then we find the index of that number in inorder (seperate left and right subtree)
    -so for each number we have to create a node and then connect them
    - then we recursively call the function to connect the left and the right side

    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])

        indx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:indx+1], inorder[:indx])

        root.right = self.buildTree(preorder[indx+1:], inorder[indx+1:])

        return root

       


        