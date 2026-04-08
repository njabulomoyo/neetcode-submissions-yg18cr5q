# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = rem = 0
        dummy = ListNode()
        curr = dummy
        #l1=[9,9,9,9,9,9,9]
        #l2=[9,9,9,9]
        while l1 or l2:
            sum = rem
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            curr.next = ListNode(sum%10)
            curr= curr.next
            rem = sum//10
        if rem:
            curr.next = ListNode(rem)


        return dummy.next
            

        