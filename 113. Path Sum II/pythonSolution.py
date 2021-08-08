# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # helper function 
        def dfs (root,current,currentSum,targetSum):
        
            if(root == None):
                return 
            currentSum+= root.val
            if (root.left == None and root.right == None):
                if(currentSum == targetSum):
                    current.append(root.val)
                    result.append(current)
                return 

            
            current.append(root.val)
        
            dfs (root.left,current.copy() ,currentSum, targetSum)
            dfs(root.right, current.copy() ,currentSum, targetSum)

        
        result =[]
        
        # helper function called
        dfs(root,[],0,targetSum)
        return result
        