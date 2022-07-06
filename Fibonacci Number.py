"""
Question:
Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        # F(n) = F(n - 1) + F(n - 2), for n > 1.
        if n > 1:
            return self.fib(n - 1) + self.fib(n - 2)
        elif n <= 1:
            return n
        # or return n if <= 1 else self.fib(n - 1) + self.fib(n - 2)
        
class Solution2:
    """
    Genius solution from leetcode discuss
    https://leetcode.com/problems/fibonacci-number/discuss/336501/Solution-in-Python-3-(beats-~100)-(three-lines)
    """
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a



def test_fib():
    s = Solution()
    n = 0
    assert s.fib(n) == 0
    n = 1
    assert s.fib(n) == 1
    n = 2
    assert s.fib(n) == 1
    n = 3
    assert s.fib(n) == 2
    n = 4
    assert s.fib(n) == 3

if __name__ == '__main__':
    test_fib() 

