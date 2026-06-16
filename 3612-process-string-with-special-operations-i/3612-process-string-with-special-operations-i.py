class Solution:
    def processStr(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i] == '*':
                if ans:
                    ans.pop()
            elif s[i] == '#':
                ans.extend(ans)
            elif s[i] == '%':
                ans=ans[::-1]
            else:
                ans.append(s[i])
        ans = "".join(ans)
        
        return ans
        