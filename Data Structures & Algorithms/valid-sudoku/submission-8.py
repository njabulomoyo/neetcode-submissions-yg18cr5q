class Solution:
    """
    Understand:
    input - 2d array
    output - boolean
    edge cases?
        - 
    Match:
     - iteration
     - lists
    
    Plan:
    1. create three sets, for rows, columns and the boxes
    2. iterate 9 times to check the rows, then the columns
    3. we can find out which box a number is in by dividing the indices by three
    4. do this till the end of the list
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:         
        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set) 
        for i in range(9):           
            for j in range(9):
                r = i//3
                c = j//3
                if board[i][j] == ".":
                    continue
                else:
                    if (board[i][j] in row[i] or 
                    board[i][j] in col[j] or
                    board[i][j] in box[(r,c)]):
                        return False

                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(r,c)].add(board[i][j])
                    
        return True
                


        