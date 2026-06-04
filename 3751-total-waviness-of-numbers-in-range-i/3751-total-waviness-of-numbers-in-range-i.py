class Solution:
    def ListOfDigits(Self, num):
        ans=[]
        while num:
            ans.append(num%10)
            num=num//10
        ans=ans[::-1]
        return ans
    def NumberOfDigits(self, num):
        count=0
        while num:
            num=num//10
            count+=1
        return count
    def getWaviness(self, num):
        if self.NumberOfDigits(num)>=3:
            digits = self.ListOfDigits(num)
            peak, valley=0,0
            for i in range(1, len(digits)-1):
                if digits[i-1]<digits[i]>digits[i+1]:
                    peak+=1
                elif digits[i-1]>digits[i]<digits[i+1]:
                    valley+=1
                else:
                    continue
            return peak+valley
        return 0
    def totalWaviness(self, num1: int, num2: int) -> int:
        Waviness=0
        for i in range(num1, num2+1):
            Waviness+=self.getWaviness(i)
        return Waviness