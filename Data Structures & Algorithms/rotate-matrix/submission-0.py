class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r

                # save topleft
                topLeft = matrix[top][l+i]

                # save bottom left in top left
                matrix[top][l+i] = matrix[bot-i][l]

                # save bottom right in bottom left
                matrix[bot-i][l] = matrix[bot][r-i]

                # save top right in bottom right
                matrix[bot][r-i] = matrix[top+i][r]

                # save top right with top left
                matrix[top+i][r] = topLeft
            
            l += 1
            r -= 1