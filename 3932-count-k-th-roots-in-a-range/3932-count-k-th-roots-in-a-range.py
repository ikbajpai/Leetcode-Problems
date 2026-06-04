class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        count=0
        if k==1:
            count =r-l+1
            return count
        for x in range(r+1):
            p=x**k
            if l<=p<=r:
                count+=1
            elif p>r:
                break
        return count
        