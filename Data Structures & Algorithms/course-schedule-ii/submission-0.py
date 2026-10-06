class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMaps = defaultdict(list)
        visit = set()
        cycle = set()
        result=[]
        for crs, pre in prerequisites:
            preMaps[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for neighbor in preMaps[crs]:
                if not dfs(neighbor): return False
            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)

            return True

            


        for i in range(numCourses):
            if not dfs(i): return []

        return result