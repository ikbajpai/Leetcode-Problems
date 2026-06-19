class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[0]
        n=len(gain)
        for i in range(n):
            ans.append(ans[i]+gain[i])


        return max(ans)