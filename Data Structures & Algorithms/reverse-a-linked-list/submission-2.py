# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:#curr = 3
            nxt = curr.next #nxt = None
            curr.next = prev #curr.next = 2
            prev = curr #prev = 3
            curr = nxt #curr = None
        
        return prev
        