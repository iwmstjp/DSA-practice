class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in nums:
                return [nums[diff]+1,i+1]
            nums[n] = i


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1
        return [i + 1, j + 1]

