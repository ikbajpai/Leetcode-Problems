# from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        # 1. Earliest possible finish time for the first ride in either category
        min_land_end = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        # 2. Evaluate Land -> Water order
        # We start the water ride at either its start time OR when the land ride finishes (whichever is later)
        land_then_water = min(max(min_land_end, s) + d for s, d in zip(waterStartTime, waterDuration))
        
        # 3. Evaluate Water -> Land order
        # We start the land ride at either its start time OR when the water ride finishes
        water_then_land = min(max(min_water_end, s) + d for s, d in zip(landStartTime, landDuration))
        
        # 4. Return the best of the two plans
        return min(land_then_water, water_then_land)