# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def BST(root,val):
            
            if(root is None):
                return
            
            if(root.val==val  ):
                return root
            
            return BST(root.left,val) or BST(root.right,val)
            
            
            return None
        
        return BST(root,val)