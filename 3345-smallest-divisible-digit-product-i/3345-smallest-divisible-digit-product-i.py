class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        mini = float('inf')
        
        def pod(i):
            prod=1
            while i:
                prod = prod * (i%10)
                i=i//10
            return prod

        for i in range(n, n+t+1):
            if pod(i)%t == 0:
                mini=i
                break
            else:
                continue
        return mini
        