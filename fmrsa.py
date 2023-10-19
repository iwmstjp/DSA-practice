class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right)//2
            print(f"left: {left}, right:{right}, middle:{middle}")
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[left] > nums[middle]:
                right = middle
            else:
                right = middle - 1
        print(f"left: {left}, right:{right}, middle:{middle}")
        return nums[left]