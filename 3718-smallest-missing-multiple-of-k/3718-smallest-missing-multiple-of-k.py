class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=k
        while 1:
            if n in nums:
                n+=k
            else:
                return n
