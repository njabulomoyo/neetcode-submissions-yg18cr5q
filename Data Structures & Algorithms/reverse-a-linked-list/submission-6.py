# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    reverse the lst and return the node

    brainstorm:

    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        a = None
        b = head
    
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        
        head = a
        
    
        return head
		