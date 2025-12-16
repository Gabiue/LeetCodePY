from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


mySolution = Solution()


mylist = [0, 1, 2]
mySolution.getConcatenation(mylist)
print(mylist)
