class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # i from starting 0 index
        # j from i+1, next to non same element
        # k starting from last element, to compensate the sum to 0
        ans=[]
        n=len(nums)
        for i in range(n):
            # skip duplicates of i
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k = n-1

            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    # skip duplicates for j
                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                    # skip duplicates for k
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                
                elif total<0:
                    j+=1
                else:
                    k-=1
        return ans