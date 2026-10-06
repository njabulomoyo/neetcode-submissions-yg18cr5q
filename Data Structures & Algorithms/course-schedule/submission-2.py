class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMaps = defaultdict(list)
        visiting = set()
        for crs, pre in prerequisites:
            preMaps[crs].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False
            if not preMaps[crs]:
                return True
                
            visiting.add(crs)
            for pre in preMaps[crs]:
                if not dfs(pre): return False

            visiting.remove(crs)
            preMaps[crs]=[]

            return True


        for i in range(numCourses):
            if not dfs(i): return False


        return True
        