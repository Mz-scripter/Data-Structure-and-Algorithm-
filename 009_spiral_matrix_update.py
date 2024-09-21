from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        answer = []
        total_num = len(matrix) * len(matrix[0])
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # Start of spiral
        while len(answer) < total_num:

            # left to right
            for n in range(left, right + 1):
                answer.append(matrix[top][n])
            top += 1

            # top to bottom
            for n in range(top, bottom + 1):
                answer.append(matrix[n][right])
            right -= 1

            # right to left
            for n in range(right, left - 1, -1):
                answer.append(matrix[bottom][n])
            bottom -= 1

            # bottom to top
            for n in range(bottom, top - 1, -1):
                answer.append(matrix[n][left])
            left += 1
        # End of spiral
        while len(answer) > total_num:
            answer.pop()
        return answer

