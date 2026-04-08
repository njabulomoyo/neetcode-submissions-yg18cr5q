# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
-Understand:
-can the list be empty? return empty list
-output- one sorted list
-time and space complexities: O(n*k) time and an O(1) space
#match
linked lists
#plan
-sort two lists at a time and then store the results in a new list
-do this till the list is left with one sorted list...

"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return 

        merged = []
        while len(lists) > 1:
            i = 0
            j = i+1
            while i < len(lists):                
                if j == len(lists) and lists[i]:
                    merged.append(lists[i])
                    i+=1
                    continue                    
                merged.append(self.mergeTwoSorted(lists[i],lists[j]))
                i += 2
                j += 2
            lists = merged
            merged = []

        return lists[0]
  

    def mergeTwoSorted(self,a,b):
        dummy = ListNode()
        curr = dummy

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        if a:
            curr.next = a
        if b:
            curr.next = b

        return dummy.next

        