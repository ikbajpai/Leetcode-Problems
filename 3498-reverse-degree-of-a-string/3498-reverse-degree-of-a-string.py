class Solution:
    def reverseDegree(self, s: str) -> int:
        res =0
        for idx, el in enumerate(s):
            reverse = 27-(ord(el)-ord('a')+1)
            res += reverse*(idx+1)
        return res
