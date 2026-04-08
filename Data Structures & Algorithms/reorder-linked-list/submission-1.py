# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        output = dummy
        slow = head
        fast = head.next
        slower = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        b = slow.next
        a = slow.next = None
                 
        while b:
            c = b.next
            b.next = a
            a = b
            b = c           

        first = head
        second = a
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        if second:
            second.next = temp2              
        #output.next = None
        #return dummy.next

        