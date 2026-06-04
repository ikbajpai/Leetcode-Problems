class Solution:
    def getWaviness(self, num):
        digits = list(map(int, str(num)))
        
        if len(digits) < 3:
            return 0
        
        peak = valley = 0
        
        for i in range(1, len(digits)-1):
            if digits[i-1] < digits[i] > digits[i+1]:
                peak += 1
            elif digits[i-1] > digits[i] < digits[i+1]:
                valley += 1
        
        return peak + valley

    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(self.getWaviness(i) for i in range(num1, num2+1))