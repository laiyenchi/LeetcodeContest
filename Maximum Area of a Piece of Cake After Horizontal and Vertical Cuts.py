"""
Question:
Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""

from typing import List


class Solution:
    """
    Time Complexity: O(h log h + v log v)
    """
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # sort lists
        horizontalCuts.sort() # O(n log n)
        verticalCuts.sort() # O(n log n)
        
        # insert the first index and last index to the lists
        horizontalCuts.insert(0, 0) # O(1)
        horizontalCuts.insert(len(horizontalCuts), h) # O(1)
        verticalCuts.insert(0, 0) # O(1)
        verticalCuts.insert(len(verticalCuts), w) # O(1)
        # alternative code: sorted([0] + horizontalCuts + [h])


        # find the max gap in the lists
        max_gap_h = max([horizontalCuts[i] - horizontalCuts[i-1] for i in range(1, len(horizontalCuts))]) # max is O(n), for loop is O(n)
        max_gap_v = max([verticalCuts[i] - verticalCuts[i-1] for i in range(1, len(verticalCuts))])

        return ( max_gap_h * max_gap_v ) % (1000000000 + 7)




def test_maxArea():
    s = Solution()
    h = 5
    w = 4
    horizontalCuts = [1,2,4]
    verticalCuts = [1,3]
    assert s.maxArea(h,w,horizontalCuts, verticalCuts) == 4
    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]
    assert s.maxArea(h,w,horizontalCuts, verticalCuts) == 6
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    assert s.maxArea(h,w,horizontalCuts, verticalCuts) == 9
    h = 1000000000
    w = 1000000000
    horizontalCuts = [2]
    verticalCuts = [2]
    assert s.maxArea(h,w,horizontalCuts, verticalCuts) == 81



if __name__ == "__main__":
    test_maxArea()
