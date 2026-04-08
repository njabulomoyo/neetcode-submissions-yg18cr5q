class Solution:
    """
    understand:
    input - list of lists
    output - boolean
    plan:
        1. create three sets, for rows, columns and boxes
        2. start with the rows, check if the are any duplicate
        3. then rows and then boxes
        4. to get the boxes we can use the the indices of the rows and columns.
        divide them by 3 to see which box a certain square belongs to. 


    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:       
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rows:
                    return False
                rows.add(board[i][j])

        print("rows")
        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in cols:
                    return False
                cols.add(board[j][i])
        print("cols")

        d = defaultdict(set)
        for i in range(9):
            for j in range(9):
                col = j//3
                row = i//3
                key = tuple([row,col])
                if board[i][j] == ".":
                    continue
                elif board[i][j] in d[(row,col)]:
                    return False
                d[(row,col)].add(board[i][j])

        return True


                







