class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = set()

        def turnZero(row, col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
            
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroes.add((r,c))
        
        for rc in zeroes:
            turnZero(rc[0], rc[1])