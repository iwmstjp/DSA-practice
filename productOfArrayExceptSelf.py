class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = 1
        for n in nums:
            answer.append(prefix)
            prefix *= n
        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            answer[index] = answer[index] * postfix
            postfix *= nums[index]
        return answer