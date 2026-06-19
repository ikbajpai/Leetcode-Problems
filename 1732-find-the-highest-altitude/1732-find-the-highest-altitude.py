class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        maxi=0
        n=len(gain)
        for i in range(n):
            ans+=gain[i]
            maxi=max(maxi, ans)        
        return maxi