class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                first, last = matrix[r][0] , matrix[r][-1]
                if last < target:
                    break
                elif matrix[r][c] == target:
                    return True
                else:
                    continue
        return False
