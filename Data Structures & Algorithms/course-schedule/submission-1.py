class Solution:
    """
    output: bool

    brainstorm:
    - inititiate a hasmap for the courses and theri prerequisites
    - then iterate thru the list using recursion, 
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = defaultdict(list)
        for crs, prereq in prerequisites:
            courses[crs].append(prereq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if courses[crs] == []:
                return True

            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre): return False

            visited.remove(crs)
            courses[crs] = []
            return True


        for c in range(numCourses):
            if not dfs(c): return False

        return True
                


        

        