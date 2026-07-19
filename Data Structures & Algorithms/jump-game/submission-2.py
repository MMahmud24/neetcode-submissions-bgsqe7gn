class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = len(nums) - 1
        curr = x

        for i in range(1, x+1):
            if (x - i) + nums[x-i] >= curr:
                curr = x - i

        if curr == 0:
            return True

        return False
            
            
