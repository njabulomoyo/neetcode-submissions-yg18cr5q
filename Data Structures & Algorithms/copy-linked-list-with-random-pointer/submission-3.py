"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copiedList = {None:None}
        cur = head
        while cur:
            copiedList[cur] = Node(cur.val)
            cur = cur.next

        newCur = head
        while newCur:
            copiedList[newCur].next = copiedList[newCur.next]
            copiedList[newCur].random = copiedList[newCur.random]
            newCur = newCur.next

        return copiedList[head]
        