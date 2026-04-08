# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        

        prev = dummy
        num = count - n
        while num > 0:
            prev = prev.next
            num -= 1
        
        prev.next = prev.next.next
        return dummy.next
            



