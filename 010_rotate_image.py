import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given n x n 2D matrix by 90 degrees clockwise in-place.
        
        Args:
            matrix: A square matrix represented as a list of lists
        
        Raises:
            ValueError: If matrix is empty, None, or not square
        """

        if not matrix or not matrix[0]:
           raise ValueError("Matrix cannot be empty")
        n = len(matrix)
        if any(len(row) != n for row in matrix):
            raise ValueError("Matrix must be square")
        
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()


class TestMatrixRotation(unittest.TestCase):
    def test_rotate_matrix(self):
        solution = Solution()
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        solution.rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_edge_cases(self):
        solution = Solution()
        
        # Test 1 x 1 matrix
        matrix_1x1 = [[1]]
        solution.rotate(matrix_1x1)
        self.assertEqual(matrix_1x1, [[1]])

        # Test empty matrix
        with self.assertRaises(ValueError):
            solution.rotate([])
        
        # Test larger matrix
        matrix_5x5 = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected_5x5 = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
        solution.rotate(matrix_5x5)
        self.assertEqual(matrix_5x5, expected_5x5)


if __name__ == '__main__':
    unittest.main()


