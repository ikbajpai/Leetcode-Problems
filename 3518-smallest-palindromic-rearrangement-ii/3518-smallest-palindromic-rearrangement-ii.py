from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        freq = Counter(s)

        # Check palindrome feasibility
        odd = 0
        mid = ""
        half = [0] * 26

        for ch, cnt in freq.items():
            if cnt & 1:
                odd += 1
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2

        if odd > 1:
            return ""

        m = len(s) // 2

        def count(cnt, total):
            """Number of distinct permutations of the multiset."""
            ans = 1
            rem = total

            for x in cnt:
                if x:
                    ans *= comb(rem, x)
                    if ans >= LIMIT:
                        return LIMIT
                    rem -= x

            return ans

        if count(half, m) < k:
            return ""

        left = []
        remaining = m

        while remaining:
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = count(half, remaining - 1)

                if ways >= k:
                    left.append(chr(c + ord('a')))
                    remaining -= 1
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]