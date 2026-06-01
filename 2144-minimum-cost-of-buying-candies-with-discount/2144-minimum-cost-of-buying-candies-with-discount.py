class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost=0
        cost.sort()
        for i in range(1, len(cost)+1):
            if i%3==0:
                continue
            else:
                min_cost+=cost[len(cost)-i]
        return min_cost