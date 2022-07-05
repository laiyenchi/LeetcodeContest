"""
Question:
Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # find the min number
        start = min(nums)
        
        # remove duplicates and sort nums list
        sorted_nums = list(dict.fromkeys(nums))
        sorted_nums.sort()

        counter = 0
        results = []
        while len(sorted_nums) > 0:
            if start == sorted_nums[0]:
                start += 1
                counter += 1
                sorted_nums.remove(sorted_nums[0])
            else:
                results.append(counter)
                start = sorted_nums[0]
                counter = 0

        results.append(counter)

        return max(results)


def test_longestConsecutive():
    s = Solution()
    nums = [100,4,200,1,3,2]
    assert s.longestConsecutive(nums) == 4
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert s.longestConsecutive(nums) == 9
    nums = []
    assert s.longestConsecutive(nums) == 0
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    assert s.longestConsecutive(nums) == 7
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
    assert s.longestConsecutive(nums) == 4
    nums = [1,2,0,1]
    assert s.longestConsecutive(nums) == 3


if __name__ == "__main__":
    # nums = [1,2,0,1]
    # print(Solution().longestConsecutive(nums))
    test_longestConsecutive()