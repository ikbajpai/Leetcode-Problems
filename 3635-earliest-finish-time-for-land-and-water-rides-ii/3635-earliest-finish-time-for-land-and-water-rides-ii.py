class Solution:
    def solve(self, A_start, A_dur, B_start, B_dur):
        idxs = sorted(range(len(B_start)), key=lambda i: B_start[i])
        
        bs = [B_start[i] for i in idxs]
        bd = [B_dur[i] for i in idxs]
        m = len(bs)
        
        suffix = [0]*m
        suffix[-1] = bs[-1] + bd[-1]
        for i in range(m-2, -1, -1):
            val = bs[i] + bd[i]
            suffix[i] = val if val < suffix[i+1] else suffix[i+1]
        
        prefix = [0]*m
        prefix[0] = bd[0]
        for i in range(1, m):
            prefix[i] = bd[i] if bd[i] < prefix[i-1] else prefix[i-1]
        
        ans = float('inf')
        
        for i in range(len(A_start)):
            endA = A_start[i] + A_dur[i]
            idx = bisect.bisect_left(bs, endA)
            
            if idx < m:
                ans = min(ans, suffix[idx])
            if idx > 0:
                ans = min(ans, endA + prefix[idx-1])
        
        return ans
    
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(
            self.solve(landStartTime, landDuration, waterStartTime, waterDuration),
            self.solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )