from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        # This sorts the list based on the first number in each interval
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                # The if condition checks if the merged list is empty or if the 2nd number in the last
                # interval of merged list is less than the starting number in the interval list
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        #         If there is overlap, the last list in the merged will be replaced by the starting
        #         of the merged list since that is the smallest, and the ending will be replaced by
        #         the maximum of the second number in the merged list and interval
        return merged


#     Time complexity: O(n logn)
#     Space Complexity: O(n)

result = Solution()
print(result.merge([[1,4],[4,5]]))
