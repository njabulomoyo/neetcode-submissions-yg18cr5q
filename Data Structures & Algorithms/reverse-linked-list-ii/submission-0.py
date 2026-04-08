# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(next=head)
        slow = dummy

        for _ in range(left-1):
            slow = slow.next
        
        end = slow.next
        prev = None
        cur = end

        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        slow.next = prev
        end.next = cur

        return dummy.next












