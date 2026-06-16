class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            str_x = str(x)
            n=len(str_x)
            for i in range(n//2):
                if str_x[i] != str_x[n-i-1]:
                    return False
            return True