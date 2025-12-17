class Solution:
    def romanToInt(self, s: str) -> int:
        RomanNums = {'I': 1,
                     '0': 0,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        listRoman = list(s)
        sum = 0
        i = 0
        while i < len(listRoman):

            if i == len(listRoman)-1:
                sum += RomanNums[listRoman[i]]
                break

            if RomanNums[listRoman[i]] < RomanNums[listRoman[i+1]] and i+1 <= len(listRoman):
                sub = RomanNums[listRoman[i+1]] - RomanNums[listRoman[i]]
                sum += sub
                i += 2

            else:
                sum += RomanNums[listRoman[i]]
                i += 1
        return sum
