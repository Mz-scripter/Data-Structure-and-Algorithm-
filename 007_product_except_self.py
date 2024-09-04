from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize variables to keep track of the cumulative product from the left and right
        l_mult = 1
        r_mult = 1

        # Get the length of the input list
        n = len(nums)

        # Initialize two arrays to store the products from the left and right
        l_arr = [0] * n
        r_arr = [0] * n

        # First pass: Calculate the left and right products
        for i in range(n):
            j = -i - 1  # Negative index to move from the end of the array

            # Store the cumulative product from the left up to index i
            l_arr[i] = l_mult

            # Store the cumulative product from the right up to index j
            r_arr[j] = r_mult

            # Update the cumulative products
            l_mult *= nums[i]  # Multiply by the current element for the left product
            r_mult *= nums[j]  # Multiply by the current element for the right product

        # Combine the left and right products for the final result
        return [l * r for l, r in zip(l_arr, r_arr)]
