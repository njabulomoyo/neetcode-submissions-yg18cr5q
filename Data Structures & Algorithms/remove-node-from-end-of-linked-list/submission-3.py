# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1
        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next
        return dummy.next

        
        
        '''
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        elim = count - n 
        dummy = ListNode(next=head)
        curr = dummy
        while elim > 0:
            curr = curr.next
            elim -= 1
        curr.next = curr.next.next

        return dummy.next
        '''

        