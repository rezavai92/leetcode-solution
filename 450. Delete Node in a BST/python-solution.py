# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMinimum (self,root):
        
        if(root.left is None ):
            return root
        if (root.right is None ):
            return root.left
        
        return self.findMinimum(root.left)
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if (root is None):
            return root
        
        elif (key<root.val):
            root.left=self.deleteNode(root.left,key)
            
        elif (key > root.val):
            root.right =self.deleteNode(root.right,key)
        else:
            if (root.left is None and root.right is None):
                
                root=None
                
            elif(root.left is None):
                
                root= root.right
                                
            elif (root.right is None):
                root = root.left
                
            else:
                
                tmp = self.findMinimum(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right,tmp.val)
        return root
            