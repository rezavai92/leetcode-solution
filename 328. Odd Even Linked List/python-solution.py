# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=1
        current = head
        oddHead = ListNode()
        
        evenHead = ListNode()
    
        currentOdd = oddHead
        currentEven = evenHead
        while(current is not None):
            if(i%2 ):
                currentOdd.next=current
                currentOdd = current
            else:
                currentEven.next = current
                currentEven=current
            current = current.next
            i+=1
        currentEven.next = None
        #print(evenHead.next)
        currentOdd.next = evenHead.next
        

        return oddHead.next
        