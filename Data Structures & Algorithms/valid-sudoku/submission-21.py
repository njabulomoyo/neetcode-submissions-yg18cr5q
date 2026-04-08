class Solution:
    """
    output - boolean
    solution:
    iterate thru the 2d array,
    initiate some storage for the rows, cols and boxes (hashMap)
    for each elem, check if there is a duplicate inside the storages
    if there is a duplicate, then return False
    if not, continue. 
    if we come across a period, continue
    do this until the end of the array
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                r = i//3
                c = j//3
                num = board[i][j]
                if num == ".":
                    continue
                elif num in row[i]:
                    return False
                elif num in col[j]:
                    return False
                elif num in box[(r,c)]:
                    return False
            
                row[i].add(num)
                col[j].add(num)
                box[(r,c)].add(num)

        return True
