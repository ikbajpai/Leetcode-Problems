class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        water = sorted(zip(waterStartTime, waterDuration))
        ws = [x[0] for x in water]
        wd = [x[1] for x in water]
        m = len(water)
        
        # suffix min of (start + duration)
        suffix = [0]*m
        suffix[-1] = ws[-1] + wd[-1]
        for i in range(m-2, -1, -1):
            suffix[i] = min(suffix[i+1], ws[i] + wd[i])
        
        # prefix min of duration
        prefix = [0]*m
        prefix[0] = wd[0]
        for i in range(1, m):
            prefix[i] = min(prefix[i-1], wd[i])
        
        ans = float('inf')
        
        # Try Land → Water
        for i in range(len(landStartTime)):
            endLand = landStartTime[i] + landDuration[i]
            
            idx = bisect.bisect_left(ws, endLand)
            
            # Case: water starts after
            if idx < m:
                ans = min(ans, suffix[idx])
            
            # Case: water already open
            if idx > 0:
                ans = min(ans, endLand + prefix[idx-1])
        
        # 🔁 Repeat SAME logic swapping roles (Water → Land)
        
        land = sorted(zip(landStartTime, landDuration))
        ls = [x[0] for x in land]
        ld = [x[1] for x in land]
        n = len(land)
        
        suffix = [0]*n
        suffix[-1] = ls[-1] + ld[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], ls[i] + ld[i])
        
        prefix = [0]*n
        prefix[0] = ld[0]
        for i in range(1, n):
            prefix[i] = min(prefix[i-1], ld[i])
        
        for j in range(len(waterStartTime)):
            endWater = waterStartTime[j] + waterDuration[j]
            
            idx = bisect.bisect_left(ls, endWater)
            
            if idx < n:
                ans = min(ans, suffix[idx])
            
            if idx > 0:
                ans = min(ans, endWater + prefix[idx-1])
        
        return ans