from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0]*(mx+1)
        for x in nums:
            freq[x]+=1
        
        cnt = [0]*(mx+1)

        for d in range(1, mx+1):
            for multiple in range(d, mx+1, d):
                cnt[d]+=freq[multiple]

        # count pairs divisible by d

        exact=[0]*(mx+1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            exact[d] = c*(c-1)//2
            for multiple in range(2*d, mx+1, d):
                exact[d]-=exact[multiple]

        prefix = [0]
        total=0

        for g in range(1, mx+1):
            total+=exact[g]
            prefix.append(total)
        
        ans=[]
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans
        
        
        
        # n = len(nums)
        # m=len(queries)
        # gcdPair=[]
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         gcdPair.append([self.gcd(nums[i], nums[j])])
        # gcdPair.sort()
        # ans=[]

        # for i in range(m):
        #     ans.extend(gcdPair[queries[i]])
        # return ans