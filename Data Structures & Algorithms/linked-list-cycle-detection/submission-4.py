# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    output: bool

    brainstorm:
    - iterate thru the list to find the cycle
    - use a slow and fast pointer 

    edge cases?
    - empty input? return False
    - 

    solution:
    use a fast and slow pointer 
    fast pointer starts ahead
    iterate until it reaches the end
    - if it actually hits the end, return false, if at some point
    fast == slow, then there is a cycle, return true
    will the values on the nodes be uniq?
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast.val == slow.val:
                return True


        return False


