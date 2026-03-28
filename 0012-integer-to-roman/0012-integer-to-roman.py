class Solution:
    def intToRoman(self, num: int) -> str:
        # We explicitly add the "4s" and "9s" to our rules
        roman_values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        l = []
        
        for val, symbol in roman_values:
            while num >= val:
                l.append(symbol)
                num -= val
                
        return "".join(l)