class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def digit(n):
            lis=[0,1]
            while n>0:
                lis[0]+=n%10
                lis[1]*=n%10
                n=n//10
            return sum(lis)
        # def digitProd(n):
        #     prod=1
        #     while n>0:
        #         prod*=n%10
        #         n=n//10
        #     return prod
        return True if n%(digit(n))==0 else False