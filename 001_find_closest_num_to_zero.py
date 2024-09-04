from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest


# Time complexity: 0(n)
# Space complexity: 0(1)
nums = [-4, 7, 5, 4, 8]
solution = Solution()
result = solution.findClosestNumber(nums)
print(result)
