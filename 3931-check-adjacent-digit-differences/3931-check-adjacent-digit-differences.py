class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        def digitsInList(x):
            d=list(map(int, s))
            return d
        def f(x):
            if len(x)<3:
                return True if (abs(x[0]-x[1])<=2) else False
            for i in range(1,len(x)-1):
                if abs(x[i]-x[i-1]) >2 or abs(x[i]-x[i+1])>2:
                    return False
            return True
        return f(digitsInList(s))

        