class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Handle empty string after spaces
        if i == n:
            return 0
        
        # 3. Handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # 4. Convert digits
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 5. Overflow check BEFORE adding digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result