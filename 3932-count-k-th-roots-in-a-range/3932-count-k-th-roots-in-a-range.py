import math
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def floor(n):
            low, high= 0,n+1
            while(low+1<high):
                mid= (low+high)//2
                if(pow(mid,k)<=n):
                    low= mid
                else:
                    high= mid
            return low
        if(l==0):
            return floor(r)+1
        return floor(r)-floor(l-1)

# class Solution:
#     def countKthRoots(self, l: int, r: int, k: int) -> int:
#         count=0
#         if k==1:
#             count =r-l+1
#             return count
#         for x in range(r+1):
#             p=x**k
#             if l<=p<=r:
#                 count+=1
#             elif p>r:
#                 break
#         return count
        