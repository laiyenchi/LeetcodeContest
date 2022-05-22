"""
Problem:
Percentage of Letter in String
https://leetcode.com/contest/weekly-contest-294/problems/percentage-of-letter-in-string/
https://leetcode.com/problems/percentage-of-letter-in-string/
"""
from collections import Counter
import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        result = Counter(s)
        letter_count = result.get(letter, 0)
        percentage = math.floor(letter_count / len(s) * 100)
        return percentage

s = "foobar"
letter = "o"
s = "jjjj"
letter = "k"
print(Solution().percentageLetter(s, letter))