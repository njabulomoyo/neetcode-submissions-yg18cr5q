# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        list1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        a = slow.next
        s = slow.next = None

        while a:
            b = a.next
            a.next = s
            s = a
            a = b
        
        list2 = s
        print(list1)
        print(list2)
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2

        

        

        