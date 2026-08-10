from functools import cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dp(i):
            if i==0:
                return False

            for j in range(1, isqrt(i)+1):
                if not dp(i-j**2):
                    return True
            return False
        return dp(n)