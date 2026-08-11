class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tot = nums[0]
        found = False
        for i, num in enumerate(nums):
            next = i+1

            if not found:
                if next<len(nums) and nums[next] == num+1:
                    tot+=nums[next]
                else:
                    found = True
                
        ans=tot
        while ans in nums:
            ans+=1
        return ans