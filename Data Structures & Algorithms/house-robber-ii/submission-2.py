class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])
        dp = [0] * (n-1)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for i in range(2,n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        new_arr = nums[1:]
        dp2 = [0] * (n-1)
        dp2[0] = new_arr[0]
        dp2[1] = max(new_arr[1], dp2[0])

        for i in range(2, n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + new_arr[i])

        return max(dp2[-1], dp[-1])


