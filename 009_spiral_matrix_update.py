from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        answer = []
        i = 0
        j = -1

        # Spiral
        while len(answer) < width * height:
            # Left to Right
            for m in matrix[i]:
                if m not in answer:
                    answer.append(m)

            # Top to bottom
            for m in matrix:
                if m[j] not in answer:
                    answer.append(m[j])

            # Right to Left
            for m in matrix[j][::-1]:
                if m not in answer:
                    answer.append(m)

            # Bottom to Top
            for m in matrix[::-1]:
                if m[i] not in answer:
                    answer.append(m[i])
            i += 1
            j -= 1
        return answer
        # End of Spiral