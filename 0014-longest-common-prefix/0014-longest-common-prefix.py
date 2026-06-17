class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort()
        first = strs[0]
        last=strs[-1]
        n=len(min(strs, key = len))
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans+=first[i]
        return ans
