class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f=[0]*10
        for d in digits:
            f[d]+=1
        res=0
        for n in range(100, 999, 2):
            i, remainder = divmod(n, 100)
            j, k = divmod(remainder, 10)
            
            res+=f[i]>0 and f[j]>(i==j) and f[k]>(i==k)+(j==k)

        return res