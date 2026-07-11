# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    edge cases:
    - if the list/head is empty? return None
    
    Solution:
    Traverse thru the list:
    - have three pointer, one starting behind the head, another on the head and another after the head
    - then move the points as you are traversing thru the nodes on the list
    - the head node will point to the node behind, 
    - the we move the pointers, node behind moves to the head
    - head moves to node after and node after becomes node after.nxt
    - do this until we reach the end
    - then return the head

    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev= None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head = prev
        return head

