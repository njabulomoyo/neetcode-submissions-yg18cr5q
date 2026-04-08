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
        d = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(9):
            for j in range(9):
                col = j//3
                row = i//3
                if board[i][j] == ".":
                    continue

                elif (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in d[(row,col)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                d[(row,col)].add(board[i][j])

        return True