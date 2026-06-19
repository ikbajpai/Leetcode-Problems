class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x, -n)

        half = self.myPow(x, n//2)

        # recursive case
        if n%2:
            return x*half*half
        else:
            return half * half

        