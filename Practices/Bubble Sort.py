"""
Bubble Sort
"""

from typing import List


class Solution:
    def bubble_sort(self, l:List) -> List:
        sorted_count = 0
        while sorted_count < len(l) - 1:
            unsorted_count = len(l) - sorted_count
            for i in range(unsorted_count - 1):
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
            sorted_count += 1    
        return l        


class Solution2:
    def sorting(self, l:List, sort_count:int) -> List:
        # if the sort count equals length of list minus two, means the last pair left
        if sort_count < len(l) - 1:
            unsort = len(l) - sort_count
            swap = False
            # just compare unsort items
            for i in range(unsort - 1):
                if l[i] > l[i + 1]:
                    swap = True
                    l[i], l[i + 1] = l[i + 1], l[i]
            # if swap is False, all the items are sorted 
            if swap:
                return self.sorting(l, sort_count + 1)
            else:
                return l
        else:
            return l

    def bubble_sort(self, l:List) -> List:
        return self.sorting(l, 0)

l = [5,6,9,4,7,3,8,2,1,0]
l = [4, 5, 6, 9]
print(Solution2().bubble_sort(l))    