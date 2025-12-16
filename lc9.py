class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverseNum = num[::-1]
        if (num == reverseNum):
            return True
        else:
            return False


mySolution = Solution()
int = input()
print(mySolution.isPalindrome(int))
