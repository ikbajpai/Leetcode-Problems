class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                ch_lower = ch.lower()
                if ch_lower not in first_upper:
                    first_upper[ch_lower] = i

        count = 0
        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                count += 1

        return count