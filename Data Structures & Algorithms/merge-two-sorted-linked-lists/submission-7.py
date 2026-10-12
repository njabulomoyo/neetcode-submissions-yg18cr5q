# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    output - linked list - head node
    use two pointers, one for each list
    check which number is bigger, add smaller num
    until one of the. lists is finished
    add the remainder of the list
    return head node
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        p1 = list1
        p2 = list2
        dummy = ListNode()
        cur = dummy
        while p1 and p2:
            if p1.val > p2.val:
                cur.next = p2
                p2 = p2.next
            else:
                cur.next = p1
                p1 = p1.next

            cur = cur.next

        if p1:
            cur.next = p1
        if p2:
            cur.next = p2

        return dummy.next


        