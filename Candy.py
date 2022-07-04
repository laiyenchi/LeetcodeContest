
"""
Question:
Candy
https://leetcode.com/problems/candy/

Solution:
https://www.youtube.com/watch?v=Ya-LfQ0OBkU
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # store the previous rating and candies
        prev_item = [ratings[0], 1]
        # store candy numbers
        candies = [1]
        # store current candy number
        current_candy = 0
        # check from left to right
        for idx, rate in enumerate(ratings[1:]):
            current_candy = 1
            # if the current rate is greater, increase candy number
            if rate > prev_item[0]:
                if current_candy <= prev_item[1]:
                    current_candy = prev_item[1] + 1

            # append to the candy list
            candies.append(current_candy)
            # update the previous item
            prev_item = [rate, current_candy]
            
        # check from right to left
        for i in range(len(ratings)-2,-1,-1):
            current_candy = candies[i]
            # check whether the current rate is greater
            if ratings[i] > prev_item[0] :
                # if the current candy number is smaller, increase candy number
                if current_candy <= prev_item[1]:
                    current_candy = prev_item[1] + 1
            
            # update the current candy number
            candies[i] = current_candy
            # update the previous item
            prev_item = [ratings[i], current_candy]
        return sum(candies)



def test_candy():
    s = Solution()
    ratings = [1,0,2]
    assert s.candy(ratings) == 5
    ratings = [1,2,2]
    assert s.candy(ratings) == 4
    ratings = [1,2,87,87,87,2,1]
    assert s.candy(ratings) == 13    
    ratings = [29,51,87,87,72,12]
    assert s.candy(ratings) == 12    

if __name__ == '__main__':
    test_candy()
    # ratings = [29,51,87,87,72,12]
    # print(Solution().candy(ratings))


