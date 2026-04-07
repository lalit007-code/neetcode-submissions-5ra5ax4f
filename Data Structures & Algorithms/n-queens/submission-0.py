class Solution:

    def isSafe(self,row,col,n,board):
        # checking left , because traveling left to right
        #checking diagonl upwards
        r = row
        c = col
        while r>=0 and c >=0:
            # print(board)
            # print(r,c)
            # print(board[r][c])
            if board[r][c] == 'Q':
                return False
            r-=1
            c-=1
        
        r = row
        c = col
        # checking in left direction
        while c>=0:
            if board[r][c] == 'Q':
                return False
            c-=1
        

        r = row
        c = col
        # checking diagonal downwards
        while r<n and c>=0:
            if board[r][c] == 'Q':
                return False
            r+=1
            c-=1
        
        return True


    def solve(self,col,ds,n,board):
        if col == n:
            # board.append(ds.copy())
            temp = ["".join(row) for row in board]
            ds.append(temp)
            return
        
        for row in range(n):
            if(self.isSafe(row,col,n,board)):
                board[row][col] = 'Q'
                self.solve(col+1,ds,n,board)
                board[row][col] = "."

            


    def solveNQueens(self, n: int) -> List[List[str]]:
        ds = []
        board = [['.' for _ in range(n)] for _ in range(n) ]
        # board[0][0] = 'Q'
        # print(board[0][0])

        # print(ds)
        self.solve(0,ds,n,board)
        print(board)
        print(ds)
        return ds