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
        if not head:
	        return None
        cur = head
		
        copyList = {None:None}
        while cur:
            new = Node(cur.val)
            copyList[cur] = new
            cur = cur.next

        node = head
        while node:
            copyList[node].next = copyList[node.next]
            copyList[node].random = copyList[node.random]
            node= node.next
			
        return copyList[head]