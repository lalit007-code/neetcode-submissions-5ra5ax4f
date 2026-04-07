class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # taking row and col len to ensure they stay in matrix
        row = len(board)
        col = len(board[0])
        
        #to not visit same idx
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (min(r,c) < 0 or r >= row or c >= col or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r,c))

            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))

            path.remove((r,c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): return True
        return False 