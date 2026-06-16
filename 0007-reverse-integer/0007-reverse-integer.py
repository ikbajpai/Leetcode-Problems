class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        x = abs(x)
        s=str(x)
        s=s[::-1]
        res = sign*int("".join(s))
        if res < -2**31 or res > 2**31 - 1:
            return 0
        else:
            return res