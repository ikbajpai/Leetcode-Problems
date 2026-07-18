class Solution:
    def gcd(self,x,y):
        return math.gcd(x,y)
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums),max(nums))