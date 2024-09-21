class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        answer = []
        i = 0
        j = -1

        while len(answer) < width * height:

            for m in matrix[i]:
                if m not in answer:
                    answer.append(m)

            for m in matrix:
                if m[j] not in answer:
                    answer.append(m[j])

            for m in matrix[j][::-1]:
                if m not in answer:
                    answer.append(m)

            for m in matrix[::-1]:
                if m[i] not in answer:
                    answer.append(m[i])

            i += 1
            j -= 1
        return answer

