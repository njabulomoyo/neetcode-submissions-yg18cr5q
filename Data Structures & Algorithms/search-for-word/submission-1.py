class Solution:
    """
    output: boolean
    brainstorm:
    start by finding the first letter on word
    then the next letter on word, check the left,right,down
    if you find the letter, mov to the next and so the same,
    if you dont, return False
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])
        paths = set()

        def dfs(i, r, c):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r == Rows or c == Cols or
                board[r][c] != word[i] or 
                (r,c) in paths):
                return False

            paths.add((r,c))
            res = (dfs(i+1, r+1, c) or
                    dfs(i+1, r-1, c) or
                    dfs(i+1, r, c-1) or
                    dfs(i+1, r, c+1))

            paths.remove((r,c))
            
            return res
                    
        for r in range(Rows):
            for c in range(Cols):
                if dfs(0,r,c):
                    return True

        return False



