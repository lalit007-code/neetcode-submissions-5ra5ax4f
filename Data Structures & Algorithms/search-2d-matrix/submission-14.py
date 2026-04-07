class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS,COLS =  len(matrix),len(matrix[0])
        top,bot = 0 , ROWS - 1
        while top<=bot:
            rows = (top+bot)//2
            if target < matrix[rows][0]:
                bot  = rows - 1
            elif target > matrix[rows][-1]:
                top = rows + 1
            else:
                break
        if not (top<=bot):
            return False
        l,r = 0,COLS - 1
        rows = (top+bot)//2
        while l<=r:
            mid = (l+r)//2
            if target < matrix[rows][mid]:
                r = mid - 1
            elif target > matrix[rows][mid]:
                l = mid + 1
            else :
                return True
        return False

                   