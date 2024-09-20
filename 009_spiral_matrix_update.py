from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        answer = []
        top, bottom = 0, len(matrix) - 1
        right, left = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left to right
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1

            # top to bottom
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            # right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    answer.append(matrix[bottom][j])
                bottom -= 1

            # bottom to top
            for i in range(bottom, top - 1, -1):
                answer.append(matrix[i][left])
            left += 1
        # End of Spiral
        return answer


result = Solution()
print(result.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
