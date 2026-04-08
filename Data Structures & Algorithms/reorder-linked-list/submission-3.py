# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we first need to get to the midpoint
        #we will use the hare and tortoise algorithm
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        second = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = second
            second = curr
            curr = nxt
        
        first = head
        
        while second:
            tempo1,tempo2 = first.next, second.next

            first.next = second
            second.next = tempo1

            first, second = tempo1, tempo2
        
        



        