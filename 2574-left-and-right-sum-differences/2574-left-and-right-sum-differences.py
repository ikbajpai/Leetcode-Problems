class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        ans=[]
        leftSum=[0]
        rightSum=[0]
        n=len(nums)

        for i in range(n-1):
            leftSum.append(leftSum[-1]+nums[i])
        for i in range(n-1,0,-1):
            rightSum.append(rightSum[-1]+nums[i])
        rightSum.reverse()
        
        for i in range(len(leftSum)):
            ans.append(abs(leftSum[i]-rightSum[i]))
        
        return ans