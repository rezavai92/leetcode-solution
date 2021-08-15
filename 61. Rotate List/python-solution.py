# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k ==0:
            return head

        length =0
        current = head
        while(current):
            length+=1
            current =current.next
        if(length <=1 ):
            return head
        
        if(k%length==0):
            return head
        
        slow = head
        fast = head
        for i in range(k%length):
            fast = fast.next
            
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next
            
        
        head1 = slow.next
        slow.next = None
        current = head1
        while(current.next):
            current = current.next
        current.next = head
        
        return head1
        