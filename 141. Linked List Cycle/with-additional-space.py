# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited=[]
        current = head
        while(current is not None):
            if(current in visited):
                return True
            else:
                visited.append(current)
                current=current.next
        return False
            
        