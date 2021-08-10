# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         tortoise=head
#         hare = head
#         begin=0
#         while( hare is not None and tortoise is not None ):
#             if(tortoise ==hare and begin!=0 ):
#                 return True
#             else:
#                 if(tortoise.next):
#                     tortoise=tortoise.next.next
#                 else:
#                     tortoise=tortoise.next
#                 hare=hare.next
#             begin+=1
#         return 

        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tortoise=head
        hare = head
        
        while( hare and tortoise and tortoise.next ):
            tortoise=tortoise.next.next
            hare=hare.next
            if(tortoise == hare):
                return True
        return None
        