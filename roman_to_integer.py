class Solution:
    def romanToInt(self, s: str) -> int:
        roman_conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
                     }
        num = 0
        for i, val in enumerate(s[:-1]):
            if roman_conv[s[i]] < roman_conv[s[i+1]]:
                num -=  roman_conv[s[i]]
            else:
                num += roman_conv[s[i]]
        
        num += roman_conv[s[-1]]
        
        return num
