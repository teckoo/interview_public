class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # e.g. nums[1, 2, 3, 4]
        answer = [1]*len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        # answer = [1, 1, 2, 6]

        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        return answer
