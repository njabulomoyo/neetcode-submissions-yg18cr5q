"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    - collect all the nodes and their neigbors in an adjacency list
    - for each node, create a clone of that node,
    -  explore the neighbors of that node
    - use same function
    - return node, could be any

    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_directory = {}

        def clone(node):
            if node in node_directory:
                return node_directory[node]

            copy = Node(node.val)
            node_directory[node] = copy
            for neighbor in node.neighbors:
                node_directory[node].neighbors.append(clone(neighbor))

            return copy

        return clone(node)
