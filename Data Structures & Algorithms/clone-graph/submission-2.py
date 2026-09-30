"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    output: deep copy of the 
    brainstorm: 
    - graph traversal
    - initiate a dictionary for storing new graph nodes
    - you create the new node while traversing
    - then using the dictionary, you add the neighbors of the old node to the new node
    - then you return the node
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new_graph = {}
        def dfs(node, new_graph):
            if not node:
                return None

            if node in new_graph:
                return new_graph[node]

            new_node = Node(node.val)

            new_graph[node] = new_node

            for neighbor in node.neighbors:
                new_graph[node].neighbors.append(dfs(neighbor, new_graph))


            return new_graph[node]

        
        return dfs(node, new_graph)





















