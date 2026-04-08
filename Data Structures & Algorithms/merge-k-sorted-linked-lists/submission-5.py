# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    initiate a deque
    push all the lists into the deque
    pop the front two lists and sort them
    then append the sorted list to the end
    do this until there is one list on the deque
    """    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #how can I check condition for this -> lists = [[]]
        if not lists :
            return 

        d = deque()
        for head in lists:
            d.append(head)

        while len(d) > 1:
            lst1 = d.popleft()
            lst2 = d.popleft()
            sortedList = self.mergeTwoLists(lst1, lst2)

            d.append(sortedList)

        return d[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
        





