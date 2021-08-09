# 113. Path Sum II

### description 

## <em>Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A leaf is a node with no children. </em>

<a href="https://leetcode.com/problems/path-sum-ii/" >problem link </a>


Approach : From problem description we can see that it is a DFS problem . I will solve this with a recursive algorithm. My algorithm follows these steps:

  1. Checking the current node if it is null or not . if it is null,  we will not proceed further and go back to previous function from callstack .
  2. Checking if the current node is the leaf node. If it is a leaf node , we will check whether the currentSum is equal to targetSum. If the condition results in true
    we can decide that the path from the root node to this leaf node is our desired path. we will update the  result list/array with  current path. As u can see it is a base case, we will not proceed further with current function.
   
  
  3. update the current list/array with current node value.
  4.  then two recursive calls :
 
  *  with left child
  *  with right child
     
  
