class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        stringNum = ''.join(str(x) for x in digits)
        nums = int(stringNum) + 1
        numsList = [int(x) for x in str(nums)]
        return numsList


mySolution = Solution()

digits = [1, 2, 3]
teste = mySolution.plusOne(digits)
print(teste)
