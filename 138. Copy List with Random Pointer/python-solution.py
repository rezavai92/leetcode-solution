"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        m={None : None}
        
        current = head
        while(current is not None):
            copy = ListNode(current.val)
            m[current] = copy 
            current =current.next
            
        current = head
        
        while(current):
            #print(m[current])
            copy = m[current]
            
            copy.next = m[current.next]
            
            copy.random = m[current.random]
            current = current.next
            
        #print(m[head])
        return m[head]