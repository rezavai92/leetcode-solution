/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */

 var pathSum = function(root, targetSum) {
    
    // Helper function 
    function dfs (root,current,currentSum,targetSum){
        
        if(root == null){
            return 
        }
        
        currentSum+= root.val;
        if (root.left ==null && root.right == null){
            
            if(currentSum == targetSum){
                current.push(root.val)
                result.push(current)
                return
            }
        }
        
        current.push(root.val);
        dfs(root.left,[...current],currentSum,targetSum)
        dfs(root.right,[...current],currentSum,targetSum)
           
        
    }
    
    result =[]
    // helper function called
    dfs(root,[],0,targetSum)
    
    return result;
    
};