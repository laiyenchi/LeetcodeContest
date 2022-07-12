"""
Selection Sort
"""

from typing import List


class Solution:
    def selection_sort(self, l:List) -> List:
        # find the smallest 
        start_idx = 0
        
        while start_idx < len(l) - 1:
            min_num = l[start_idx]
            min_num_idx = start_idx
            for i in range(start_idx, len(l)):
                if l[i] < min_num:
                    min_num = l[i]
                    min_num_idx = i

            #swap with the first left item
            l[min_num_idx], l[start_idx] = l[start_idx], l[min_num_idx]
            start_idx += 1
        return l


class Solution2:
    def sorting(self, l:List, start_idx:int) -> List:
        if start_idx < len(l) - 1:
            min_num = l[start_idx]
            min_num_idx = start_idx
            for i in range(start_idx, len(l)):
                if l[i] < min_num:
                    min_num = l[i]
                    min_num_idx = i
            l[start_idx], l[min_num_idx] = l[min_num_idx], l[start_idx]
            return self.sorting(l, start_idx + 1)
        else:
            return l

    def selection_sort(self, l:List) -> List:
        return self.sorting(l, 0)

class Solution3:
    def selection_sort(self, l:List) -> List:
        # find the smallest 
        for i in range(len(l)):
            min_num_idx = i
            for j in range(i + 1, len(l)):
                if l[j] < l[min_num_idx]:
                    min_num_idx = j

            #swap with the first left item
            l[i], l[min_num_idx] = l[min_num_idx], l[i]
        return l        

l = [5,6,9,4,7,3,8,2,1,0]
print(Solution3().selection_sort(l))    