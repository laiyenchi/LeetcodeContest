"""
Problem:
Maximum Bags With Full Capacity of Rocks
https://leetcode.com/contest/weekly-contest-294/problems/maximum-bags-with-full-capacity-of-rocks/
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
"""


from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # capacity minus rocks
        result = sorted([x - rocks[i] for i, x in enumerate(capacity) ])
        counter = 0
        for x in result:
            if additionalRocks >= x :
                additionalRocks -= x
                counter += 1
        return counter


class Solution2:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # capacity minus rocks
        result = sorted([c - r for c,r in zip(capacity, rocks) ])
        # Assignment Expressions: https://peps.python.org/pep-0572/
        count = len([(additionalRocks:=additionalRocks-x) for x in result if additionalRocks >= x])
        return count

# capacity = [2,3,4,5]
# rocks = [1,2,4,4]
# additionalRocks = 2
# #Expected:3

# capacity = [91,54,63,99,24,45,78]
# rocks = [35,32,45,98,6,1,25]
# additionalRocks = 17
# #Expected:1


capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2
#Expected:3

print(Solution2().maximumBags(capacity, rocks, additionalRocks))