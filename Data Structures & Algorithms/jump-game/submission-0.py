class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = len(nums) - 1
        dp = [-1] * (x+1)

        dp[0] = x
        y = 0
        for i in range(1, x+1):
            if (x - i) + nums[x-i] >= dp[y]:
                y+=1
                dp[y] = x - i

        if dp[y] == 0:
            return True

        return False
            
            
