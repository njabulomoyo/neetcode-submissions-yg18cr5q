class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
        
        for i in range(9):
            column_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in column_set:
                    return False
                column_set.add(board[j][i])
        
        box_dict = defaultdict(set)
        for i in range(9):
            for j in range(9):
                row = i//3
                col = j//3
                if board[i][j] == ".":
                    continue
                if board[i][j] in box_dict[(row,col)]:
                    return False
                box_dict[(row,col)].add(board[i][j])
        
        return True

