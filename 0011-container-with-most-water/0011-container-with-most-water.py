class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        n=len(height)
        left, right = 0, n-1

        while left<right:
            h=min(height[left], height[right])
            width = right-left
            maxi = max(maxi, width*h)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
        