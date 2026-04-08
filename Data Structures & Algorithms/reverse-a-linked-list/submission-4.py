# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    output - linkedlist
    Solution:
    - have a dummy node equal to None
    - have three pointers, one pointing at the dummy, one at
    first noe, and the other at the second node
    - then move the pointers towards the end
    - the middle pointer should point to the last point. 
    - then we mover the pointers
    - the last becomes the second, the second becomes the first,
    the first becomes the on one next to first
    - do this until the firstpointer hits None
    return the middle pointer

    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        a = None
        b = head
        #N [0,1,2,3]
        #a, b,c
        while b: #b = 
            c = b.next #c=3
            b.next = a# b.next = 2
            a = b #a=3
            b = c #b=N
      
        head = a

        return head









