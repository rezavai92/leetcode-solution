# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fakeHead= ListNode()
        fakeHead.next=head
        currentA=fakeHead
        currentB = fakeHead
        
        
            
        for i in range(n+1):
            currentA=currentA.next
        while(currentA):
            currentA=currentA.next
            currentB=currentB.next
        currentB.next=currentB.next.next
        return fakeHead.next