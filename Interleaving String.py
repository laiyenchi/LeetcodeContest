"""
Question:
Interleaving String
https://leetcode.com/problems/interleaving-string/
"""

from functools import lru_cache


class Solution:
    """
    Refer to Approach 1: Brute Force in Leetcode, but the result is Time Limit Exceeded
    https://leetcode.com/problems/interleaving-string/solution/
    """
    def is_Interleave(self, s1: str, i: int, s2: str, j: int, res: str, s3: str) -> bool:
        if res == s3 and i == len(s1) and j == len(s2): 
            return True
        ans = False
        if i < len(s1):
            ans |= self.is_Interleave(s1, i + 1, s2, j, res + s1[i], s3)
        if j < len(s2):
            ans |= self.is_Interleave(s1, i, s2, j + 1, res + s2[j], s3)
        return ans

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        return self.is_Interleave(s1, 0, s2, 0, "", s3)

class Solution_From_Discuss:
    """
    Recursion with Memoization solution from leetcode discuss
    https://leetcode.com/problems/interleaving-string/discuss/2058338/Python-Recursion-Top-Down-with-Memo
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l3!=l1+l2:
            return False
        
        @lru_cache(None)
        def dp(i,j,k):
            if i==l1 and j==l2 and k==l3:
                return True
            if i==l1 and j==l2 and k!=l3:
                return False
            ans=False
            if i<l1 and s1[i]==s3[k]:
                ans|= dp(i+1,j,k+1)
            if j<l2 and s2[j]==s3[k]:
                ans|= dp(i,j+1,k+1)
            return ans
        
        return dp(0,0,0)



def test_isInterleave():
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert s.isInterleave(s1, s2, s3) == True
    
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    assert s.isInterleave(s1, s2, s3) == False

    s1 = ""
    s2 = ""
    s3 = ""
    assert s.isInterleave(s1, s2, s3) == True

    s1 = ""
    s2 = ""
    s3 = "a"
    assert s.isInterleave(s1, s2, s3) == False


if __name__ == '__main__':
    test_isInterleave()
    # s1 = "aa"
    # s2 = "ab"
    # s3 = "aaba"
    # s1 = "ac"
    # s2 = "b"
    # s3 = "abc"
    # print(Solution().isInterleave(s1, s2, s3))
