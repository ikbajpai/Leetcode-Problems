class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost=0
        cost.sort()
        n=len(cost)
        for i in range(1, n+1):
            if i%3==0:
                continue
            else:
                min_cost+=cost[n-i]
        return min_cost