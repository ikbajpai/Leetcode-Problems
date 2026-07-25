class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(str(n))
        n.sort()
        return int(n[-1])*int(n[-2])