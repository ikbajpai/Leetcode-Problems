from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
        # Step 1: Add boundaries
        restrictions.append([1, 0])
        restrictions.append([n, n-1])
        
        # Step 2: Sort
        restrictions.sort()
        
        # Step 3: Forward pass
        for i in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[i-1]
            curr_id, curr_h = restrictions[i]
            restrictions[i][1] = min(curr_h, prev_h + (curr_id - prev_id))
        
        # Step 4: Backward pass
        for i in range(len(restrictions)-2, -1, -1):
            next_id, next_h = restrictions[i+1]
            curr_id, curr_h = restrictions[i]
            restrictions[i][1] = min(curr_h, next_h + (next_id - curr_id))
        
        # Step 5: Find max peak
        ans = 0
        
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            
            d = id2 - id1
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)
        
        return ans