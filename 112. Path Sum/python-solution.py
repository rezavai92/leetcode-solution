# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self,root,targetSum,currentSum):
        
        if(root is None):
            return False
        if (root.left is None and root.right is None):
            currentSum+= root.val
            return currentSum==targetSum
        
        
        return self.traverse(root.left,targetSum,currentSum+root.val) or self.traverse(root.right,targetSum,currentSum+root.val)
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.traverse(root,targetSum,0)
        
        
        