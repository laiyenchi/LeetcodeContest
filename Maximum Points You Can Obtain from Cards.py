"""
Problem:
Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Solution:
https://dev.to/seanpgallivan/solution-maximum-points-you-can-obtain-from-cards-2no
"""

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_output = 0
        if len(cardPoints) == k:
            max_output = sum(cardPoints)
        else:
            remove_card_count = len(cardPoints) - k
            sum_point = sum(cardPoints)
            sub_sum = sum(cardPoints[: remove_card_count])
            max_output = sum_point - sub_sum
            for i in range(1, len(cardPoints) - remove_card_count + 1):
                # sub_sum = sub_sum - cardPoints[i - 1] + cardPoints[i + remove_card_count - 1]
                sub_sum += cardPoints[i + remove_card_count - 1] - cardPoints[i - 1]
                temp_sum = sum_point - sub_sum
                # max_output = temp_sum if (temp_sum > max_output) else max_output
                max_output = max(temp_sum, max_output)
        return max_output


class FailedSolution:
    """
    Failed due to Time Limit Exceeded
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max = 0
        if len(cardPoints) == k:
            max = sum(cardPoints)
        else:
            remove_card_count = len(cardPoints) - k
            sum_point = sum(cardPoints)
            for i in range(len(cardPoints) - remove_card_count + 1):
                # Do not use sum function, which time complexity is O(n).
                temp_sum = sum_point - sum(cardPoints[i: i + remove_card_count]) 
                max = temp_sum if (temp_sum > max) else max
        return max




cardPoints = [1,2,3,4,5,6,1]
k = 3
# output : 12

# cardPoints = [2,2,2]
# k = 2
# output : 4

# cardPoints = [9,7,7,9,7,7,9]
# k = 7
# output : 55

# cardPoints = [1,79,80,1,1,1,200,1]
# k = 3
# output : 202



# cardPoints = [100,40,17,9,73,75]
# k = 3
# # output : 248


# cardPoints = [11,49,100,20,86,29,72]
# k = 4
# output : 232

# cardPoints = [1,1000,1]
# k = 1
# output : 1


print(Solution().maxScore(cardPoints, k))