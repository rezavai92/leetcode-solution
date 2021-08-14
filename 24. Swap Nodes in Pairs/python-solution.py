# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def swap(self,head):
        current = head
        fakeHead = ListNode()
        fakeHead.next=head
        prev=fakeHead
        while(current and current.next):
            
            prev.next=current.next
            current.next= current.next.next
            prev.next.next=current
            prev=current
            current=current.next
        return fakeHead.next
        
            
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swap(head)
        
    
        