class Solution:
    from collections import deque
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)

        for crs, pre in edges:
            adj[crs].append(pre)
            adj[pre].append(crs)

        q = deque()
        q.append([0,-1])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False

                q.append([neighbor, node])
                visited.add(neighbor)

        return len(visited) == n
