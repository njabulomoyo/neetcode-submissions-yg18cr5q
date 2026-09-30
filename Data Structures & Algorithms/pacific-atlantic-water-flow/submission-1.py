class Solution:
    """
    output - list of list with all the positions

    brainstorm:
    - all points on the edge flow into the ocean
    - initiate two sets, one for pacific and another for ATL
    - Add all the points on the edge to respective sets
    - we're creating two sets so that we compare the sets and what ever points that come up in both sets will be return as a set
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def check(r, c, sea, prev):
            if (r<0 or c<0 or r==Rows or
                c==Cols or (r,c) in sea or 
                heights[r][c] < prev):
                return 

            sea.add((r,c))
            prev = heights[r][c]
            check(r+1, c, sea, prev)
            check(r-1, c, sea, prev)
            check(r, c+1, sea, prev)
            check(r, c-1, sea, prev)


        for r in range(Rows):
            check(r, 0, pac, heights[r][0])
            check(r, Cols-1, atl, heights[r][Cols-1])

        for c in range(Cols):
            check(0, c, pac, heights[0][c])
            check(Rows-1, c, atl, heights[Rows-1][c])
        res=[]
        print("this is pac", pac)
        print("atl", atl)
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res











        