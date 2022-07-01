"""
Question:
Partitioning Into Minimum Number Of Deci-Binary Numbers
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        min_num = max(n)

        return min_num


n = "328"
# Output: 3


print(Solution().minPartitions(n))