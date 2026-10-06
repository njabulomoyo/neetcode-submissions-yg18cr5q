class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        preMaps = defaultdict(list)

        for crs, pre in edges:
            preMaps[crs].append(pre)
            preMaps[pre].append(crs)

        def dfs(crs, prev):
            if crs in visited:
                return False

            visited.add(crs)
            for neighbor in preMaps[crs]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor,crs): return False

            return True

        return dfs(0,-1) and len(visited)==n
