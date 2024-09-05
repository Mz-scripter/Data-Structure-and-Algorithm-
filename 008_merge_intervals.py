from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_list = []
        intervals = sorted(intervals)
        pos = -1
        if not merged_list:
            merged_list.append(intervals[0])
        for i in intervals[1:]:
            for n in range(i[0], i[1] + 1):
                if n in range(merged_list[pos][0], merged_list[pos][1] + 1):
                    if min(i) < min(merged_list[pos]):
                        min_num = min(i)
                    else:
                        min_num = min(merged_list[pos])
                    if max(i) > max(merged_list[pos]):
                        max_num = max(i)
                    else:
                        max_num = max(merged_list[pos])
                    del merged_list[pos]
                    merged_list.append([min_num, max_num])
                    break
                else:
                    merged_list.append(i)
                    break
        return merged_list


result = Solution()
output = result.merge([[1, 4], [0, 4]])
print(output)
