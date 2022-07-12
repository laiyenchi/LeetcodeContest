"""
Binary Search
"""

from math import floor
from typing import List


class Solution:
    def bianry_search(self, l:List, target:int) -> int:
        # sort list
        l.sort()

        start_idx, end_idx = 0, len(l) - 1
        mid_idx = floor((start_idx + end_idx) / 2)

        while start_idx <= end_idx:
            if l[mid_idx] == target:
                return mid_idx
            elif l[mid_idx] > target:
                end_idx = mid_idx - 1
            elif l[mid_idx] < target:
                start_idx = mid_idx + 1

            mid_idx = floor((start_idx + end_idx) / 2)
        return -1


class Solution2:
    def find_target(self, l:List, target:int, start_idx: int, end_idx:int) -> int:
        if start_idx <= end_idx:
            mid_idx = floor((start_idx + end_idx) / 2)
            if l[mid_idx] == target:
                return mid_idx
            elif target > l[mid_idx]:
                return self.find_target(l, target, mid_idx + 1, end_idx)
            elif target < l[mid_idx]:
                return self.find_target(l, target, start_idx, mid_idx - 1)
        else:
            return -1

    def bianry_search(self, l:List, target:int) -> int:
        # sort list
        l.sort()
        start_idx, end_idx = 0, len(l) - 1
        return self.find_target(l, target, start_idx, end_idx)



l = [1,2,3,4,6,7,8,9,10]
target = 5
print(Solution2().bianry_search(l, target))