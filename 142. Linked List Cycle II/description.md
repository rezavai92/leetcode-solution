#Description
<a href="https://leetcode.com/problems/linked-list-cycle-ii/" >Problem Link </a>

## Floyd Cylce Detection Algo :
for the difference of speed in tortoise and hare , if there is a cycle in the list, at one particular node, the hare and tortoise must meet. 
#### Lemma  : 
distance from head pointer to loop's beginning point is equal to the distance from the tortoise and hare's intersection point to the beginning of the loop.
#### Proof of Lemma  : 
          
<img src="https://raw.githubusercontent.com/rezavai92/leetcode-solution/main/142.%20Linked%20List%20Cycle%20II/floyd-cycle.png" alt="pic" />

Let's assume
distance covered by hare is , d= x+y
distance covered by tortoise is, 2d = X+2Y+Z

Therefore,

          2(x+y) = x+2y+z
          2x+2y  = x+2y+z
          x      = z
          
                                                                              
                                                                             
