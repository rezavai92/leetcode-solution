# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#def hasCycle(self, head: ListNode) -> bool:
        
    

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise=head
        hare = head
        isCycle=False
        while( hare and tortoise and tortoise.next ):
            
            tortoise=tortoise.next.next
            hare=hare.next
            if(tortoise == hare):
                isCycle=True
                break
        
        if(not isCycle):
            return None
        while(tortoise is not head):
            head=head.next
            tortoise = tortoise.next
        return head
        
        