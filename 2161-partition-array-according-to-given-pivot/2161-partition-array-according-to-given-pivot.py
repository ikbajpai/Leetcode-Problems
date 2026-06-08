class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans=[]
        def leftElements():
            for i in range(len(nums)):
                if nums[i]<pivot:
                    ans.append(nums[i])
            return
        def equalElements():
            for i in range(len(nums)):
                if nums[i]==pivot:
                    ans.append(nums[i])
        def rightElements():
            for i in range(len(nums)):
                if nums[i]>pivot:
                    ans.append(nums[i])
        leftElements()
        equalElements()
        rightElements()

        return ans


        