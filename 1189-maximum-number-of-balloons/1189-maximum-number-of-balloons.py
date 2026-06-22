class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=a=l=o=n=0
        for character in text:
            if character == 'b':
                b+=1
            if character == 'a':
                a+=1
            if character == 'l':
                l+=1
            if character == 'o':
                o+=1
            if character == 'n':
                n+=1
            
        return min(b, a, l//2, o//2, n)
            

        