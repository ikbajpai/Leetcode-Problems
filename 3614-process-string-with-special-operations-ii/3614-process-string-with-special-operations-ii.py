class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        
        # Step 1: compute final length
        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '#':
                length *= 2
            elif ch == '*':
                length = max(0, length - 1)
            elif ch == '%':
                continue
        
        if k >= length:
            return "."
        
        # Step 2: reverse process
        for ch in reversed(s):
            if ch == '#':
                length //= 2
                if k >= length:
                    k -= length
            elif ch == '%':
                k = length - k - 1
            elif ch == '*':
                length += 1
            else:  # letter
                length -= 1
                if k == length:
                    return ch
        
        return "."