from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        # This sorts the list based on the first number in each interval
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
        
#     Time complexity: O(n logn)
#     Space Complexity: O(n)
