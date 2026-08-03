from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        alice = bob = 0
        n = len(stoneValue)
        @cache
        def dp(i):
            if i>=n: return 0
            ans = float('-inf')
            pick=0
            for k in range(3):
                if i+k<n: pick+=stoneValue[i+k]
                ans = max(ans, pick-dp(i+k+1))
            return ans
        diff = dp(0)
        if diff>0: return "Alice"
        elif diff<0: return "Bob"
        return "Tie"