class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        forward = 1
        for i in range(len(nums)):
            res[i] = forward
            forward *= nums[i]

        reverse = 1
        offset = len(nums) - 1
        for i in range(len(nums)):
            res[offset-i] *= reverse
            reverse *= nums[offset-i]
        return res