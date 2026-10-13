class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Maps = defaultdict(list)
        for crs, pre in prerequisites:
            Maps[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if Maps[crs]==[]:
                return True

            visiting.add(crs)
            for pre in Maps[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            Maps[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        