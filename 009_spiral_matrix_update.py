from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        answer = []
        i = 0
        j = -1
        n = None
        k = 1

        # Spiral
        while len(answer) < width * height:
            # Left to Right
            for m in matrix[i]:
                if len(answer) < width * height:
                    answer.append(m)

            # Top to bottom
            for m in matrix[k:]:
                if len(answer) < width * height:
                    answer.append(m[j])

            # Right to Left
            for m in matrix[j][::-1][k:]:
                if len(answer) < width * height:
                    answer.append(m)

            # Bottom to Top
            for m in matrix[::-1][k:-k]:
                if len(answer) < width * height:
                    answer.append(m[i])
            i += 1
            j -= 1
            k += 1
        return answer
        # End of Spiral


result = Solution()
print(result.spiralOrder([[23, 18, 20, 26, 25], [24, 22, 3, 4, 4], [15, 22, 2, 24, 29], [18, 15, 23, 28, 28]]))
