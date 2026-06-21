class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if coins<cost:
                break
            else:
                count+=1
                coins-=cost
        return count







        # def dp(i):
        #     if i==len(costs):
        #         return 1
        #     pick
        #     skip

        
        