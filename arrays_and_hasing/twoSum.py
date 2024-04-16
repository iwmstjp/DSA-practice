class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for index in range(len(nums)):
            gap = target - nums[index]
            if gap in numDict:
                return [numDict[gap], index]
            else:
                numDict[nums[index]] = index