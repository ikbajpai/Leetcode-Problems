class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # base case
        if needle == "":
            return 0
        
        def strCheck(start):
            for j in range(len(needle)):
                if haystack[start + j] != needle[j]:
                    return -1
            return start
        
        for i in range(len(haystack) - len(needle) + 1):
            res = strCheck(i)
            if res != -1:
                return res
        
        return -1