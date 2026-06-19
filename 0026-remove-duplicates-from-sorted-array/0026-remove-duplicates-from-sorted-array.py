class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=[0]
        i=1
        for j in range(0,len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i+=1
            else:
                continue
        return i
