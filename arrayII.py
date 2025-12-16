from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums.insert((2*i)+1, nums.pop(n+i))
        return nums


mySolution = Solution()

myArray = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
newArray = mySolution.shuffle(myArray, n)
arrayExpected = [1, 4, 2, 3, 3, 2, 4, 1]
print(newArray)
print(arrayExpected)

print(len(myArray))
