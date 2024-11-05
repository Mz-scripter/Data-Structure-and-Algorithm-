from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()
        
        print(matrix)


result = Solution()
result.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])


