class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in rows[i]:
                        return False
                rows[i].add(board[i][j])

        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in columns[i]:
                        return False
                columns[i].add(board[j][i])

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in square[(i//3,j//3)]:
                        return False
                square[(i//3,j//3)].add(board[i][j])
        
        return True
