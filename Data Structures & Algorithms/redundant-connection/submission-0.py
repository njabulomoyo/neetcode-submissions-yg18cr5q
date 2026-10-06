class Solution:
    """
    output: a node that causes the graph to be acyclic

    brainstorm:
    - input empty? return empty list
    - connection goes both ways
    - is it certain that there will new graph will be acyclic?
    - will it only be one cycle? or multiple?
    - return the node that can be removed

    -

    solution:
    - traverse thru the graph
    - initiate a set to track all the visited nodes
    - initiate another set to keep track of the edges on the cycle
    - for each node, check the neighbors
    - if neighbors are connected to nodes on visited, add the edge to the hashset
    - if the hashset has more tha one, 
    - iterate thru the input list to see the last edge that is in the cycle hashset
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = [False] * (len(edges)+1)
        cycle = set()
        startcycle=-1
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            nonlocal startcycle
            if visited[node]:
                startcycle = node
                return True

            visited[node]=True
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node):
                    if startcycle != -1:
                        cycle.add(node)
                    if node == startcycle:
                        startcycle = -1
                    return True
            return False

        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

        return []


        













  


        








        