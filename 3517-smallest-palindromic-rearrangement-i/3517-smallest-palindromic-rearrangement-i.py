class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # answer = sortedHalf + middle + reverse(sortedHalf)
        n = len(s)

        middle = s[n // 2] if (n & 1) == 1 else ""

        htable = [0]*26

        for i in range(n//2):
            htable[ord(s[i]) - ord('a')]+=1

        half = []

        for i in range(26):
            half.append(chr(i+ord('a'))*htable[i])

        half = "".join(half)

        return half + middle + half[::-1]

        


        