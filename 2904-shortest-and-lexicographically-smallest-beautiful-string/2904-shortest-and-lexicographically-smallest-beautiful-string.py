class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        st=""
        n=len(s)
        res=[]

        for i in range(n):
            count=0
            for j in range(i,n):
                if s[j] == '1':
                    count+=1

                if count==k:
                    res.append(s[i:j+1])
                    break
        if not res:
            return ""
        else:
            return min(res, key = lambda x:(len(x),x))