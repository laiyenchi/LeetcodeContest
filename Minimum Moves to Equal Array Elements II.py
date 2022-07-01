"""
Question:
Minimum Moves to Equal Array Elements II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Solution:
https://dev.to/seanpgallivan/solution-minimum-moves-to-equal-array-elements-ii-oej

"""
from math import floor
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort the list
        nums.sort()
        
        # get the media
        # The mean is the average of a data set.
        # The mode is the most common number in a data set.
        # The median is the middle of the set of numbers.
        median_num = nums[floor(len(nums) / 2)]

        # calculate the minium moves
        minMove = 0
        for i in range(len(nums)):
            minMove += abs(nums[i] - median_num)
        
        return minMove
        
# nums = [203125577,-349566234,230332704,48321315,66379082,386516853,50986744,-250908656,-425653504,-212123143]
# Output: 2127271182

nums = [1,2,3]
# Output: 2

# nums = [1,10,2,9]
# Output: 16

# nums = [1,0,0,8,6]
# Output: 14

# nums = [1,1,1]
# Output: 0

print(Solution().minMoves2(nums))