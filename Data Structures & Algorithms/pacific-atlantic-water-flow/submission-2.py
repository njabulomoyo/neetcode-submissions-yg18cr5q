class Solution:
    """
    - find coordinates that flow to each of the oceans
    - then compare and see which ones flow to both

    - if there are no coordinates that flow to both, cant be
    - empty grid? no

    - start with the edges going up
    - check neighbor if they are greater or equal
    - add the coordinates to the sets
    - then compare the sets
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        pac = set()
        atl = set()

        def checkNeighbors(r, c, prev, visited):
            if (r<0 or c<0 or r==Rows or
                c==Cols or (r,c) in visited or
                heights[r][c] < prev):
                return 
            visited.add((r,c))
            prev = heights[r][c]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                checkNeighbors(nr, nc, prev, visited)


        for r in range(Rows):
            checkNeighbors(r, 0, -1, pac)
            checkNeighbors(r, Cols-1, -1, atl)

        for c in range(Cols):
            checkNeighbors(0, c, -1, pac)
            checkNeighbors(Rows-1, c, -1, atl)

        results = []
        for coordinate in pac:
            rw, cl = coordinate
            if coordinate in atl:
                results.append([rw,cl])


        return results
            

        
        