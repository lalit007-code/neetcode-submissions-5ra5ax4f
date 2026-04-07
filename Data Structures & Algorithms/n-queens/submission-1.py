class Solution:

    # def isSafe(self,row,col,n,board):
    #     # checking left , because traveling left to right
    #     #checking diagonl upwards
    #     r = row
    #     c = col
    #     while r>=0 and c >=0:
    #         # print(board)
    #         # print(r,c)
    #         # print(board[r][c])
    #         if board[r][c] == 'Q':
    #             return False
    #         r-=1
    #         c-=1
        
    #     r = row
    #     c = col
    #     # checking in left direction
    #     while c>=0:
    #         if board[r][c] == 'Q':
    #             return False
    #         c-=1
        

    #     r = row
    #     c = col
    #     # checking diagonal downwards
    #     while r<n and c>=0:
    #         if board[r][c] == 'Q':
    #             return False
    #         r+=1
    #         c-=1
        
    #     return True


    def solve(self,col,ds,n,board,upperDigonal,leftDigonal,leftRow):
        if col == n:
            # board.append(ds.copy())
            temp = ["".join(row) for row in board]
            ds.append(temp)
            return
        
        for row in range(n):
            if(leftRow[row] == 0 and upperDigonal[row+col] == 0 and leftDigonal[(n-1)+(col-row)]==0):
                board[row][col] = 'Q'
                leftRow[row] = 1
                upperDigonal[row+col] = 1
                leftDigonal[(n-1)+(col-row)]=1

                self.solve(col+1,ds,n,board,upperDigonal,leftDigonal,leftRow)
                board[row][col] = "."
                leftRow[row] = 0
                upperDigonal[row+col] = 0
                leftDigonal[(n-1)+(col-row)]=0


            


    def solveNQueens(self, n: int) -> List[List[str]]:
        ds = []
        board = [['.' for _ in range(n)] for _ in range(n) ]
        # board[0][0] = 'Q'
        # print(board[0][0])

        # print(ds)
        upperDigonal = [0] * (2*n - 1)
        leftDigonal  = [0] * (2*n - 1)
        
        leftRow = [0] * n
        self.solve(0,ds,n,board,upperDigonal,leftDigonal,leftRow)
        print(board)
        print(ds)
        return ds