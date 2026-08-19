class Solution:
    """
    output: bool

    edge cases: always given 9x9
    - if the elem is '.', skip

    Solution:
    - firstly, initiate default dict(set), for the col, row, and the 3x3 boxes
    -then using an nested for loop, iterate thru the list/board, checking if the number is in the col, row, or box, already
    - if true, return False, it is not a valid sodoku
    - other continue
    - continue til the end

    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowD = defaultdict(set)
        colD = defaultdict(set)
        boxD = defaultdict(set)

        for row in range(9):
            for col in range(9):
                r = row//3
                c = col//3
                if board[row][col] == ".":
                    continue

                if (board[row][col] in rowD[row] or
                    board[row][col] in colD[col] or
                    board[row][col] in boxD[(r,c)]):
                    return False

                rowD[row].add(board[row][col])
                colD[col].add(board[row][col])
                boxD[(r,c)].add(board[row][col])

        return True
                


                




