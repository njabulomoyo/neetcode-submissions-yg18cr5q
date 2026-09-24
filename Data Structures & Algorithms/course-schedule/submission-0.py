class Solution:
    """
    output: bool

    brainstorm:
    - we need to see which course have which prerequisites
    - we need to see if there is no cycle that would prevent from finishing the course

    Sokution:
    - initiate a hashmap, capture all the courses and their prerequsites 
    - initiate set for storing the course paths
    - create a helper function to check if curr course has a prerequisite that is already in the path
    - is it does, return False
    - else check all the other elements
    - return true
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        visited = set()

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False

            visited.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            prereqs[crs]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True












        