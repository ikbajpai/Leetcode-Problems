class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        return diff*k