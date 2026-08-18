from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []
        freq=Counter()
        for i in range(n-k+1):
            seen = set()

            for j in range(i, i+k):
                seen.add(nums[j])
            
            for x in seen:
                freq[x]+=1
        ans=-1
        for x in freq:
            if freq[x] == 1:
                ans = max(ans, x)
        return ans
                

