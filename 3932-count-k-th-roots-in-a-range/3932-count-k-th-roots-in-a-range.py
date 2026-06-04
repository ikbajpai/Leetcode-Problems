class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        count=0
        if k==1:
            count =r-l+1
            return count
        for x in range(r+1):
            if l<=x**k<=r:
                count+=1
            elif x**k>r:
                break
        return count
        