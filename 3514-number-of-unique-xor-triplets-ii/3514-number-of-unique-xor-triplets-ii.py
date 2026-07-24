class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048

        dp = [False] * MAX_XOR
        dp[0] = True

        for _ in range(3):
            ndp = [False] * MAX_XOR
            for x in range(MAX_XOR):
                if dp[x]:
                    for num in nums:
                        ndp[x ^ num] = True
            dp = ndp

        return sum(dp)