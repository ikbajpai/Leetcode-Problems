class Solution:

    def sumOfDigits(self, nums):
        temp=0
        while nums>0:
            temp += nums%10
            nums = nums//10
        return temp


    def minElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[i] = self.sumOfDigits(nums[i])
        return min(nums)
        