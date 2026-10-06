class Solution:
    """
    output: int

    brainstorm:
    - undirected graph, goes both ways 
    - create an adjacency mapping
    - initiate set to check the visited numbers
    - have a helper function to check out all the components that are connected, 
    - each time all the connected components are finished, add 1 to a count variable
    - return that variable
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        connected = 0
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visited:
                return 

            visited.add(i)
            for neighbor in adj[i]:
                if neighbor == prev:
                    continue
                dfs(neighbor, i)
                
            return 

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                connected += 1

        return connected
