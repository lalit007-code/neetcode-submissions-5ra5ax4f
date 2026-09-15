from collections import defaultdict

class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        board = defaultdict(set)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == ".":
                    continue

                if matrix[i][j] in row[i] or matrix[i][j] in col[j] or   matrix[i][j] in board[i//3*3+ j//3]:
                    return False

                row[i].add(matrix[i][j])
                col[j].add(matrix[i][j])
                board[i//3*3+ j//3].add(matrix[i][j])

        # print("row", row)
        # print("col", col)
        # print("board", board)

        return True