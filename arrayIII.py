from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                count = 0
            else:
                count += 1
            if (count > maxCount):
                maxCount = count
        return maxCount


mySolution = Solution()

nums = [1, 1, 0, 1, 1, 1]


print(mySolution.findMaxConsecutiveOnes(nums))
