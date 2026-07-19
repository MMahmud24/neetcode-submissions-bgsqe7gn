class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        
        dp = [0] * (amount + 1)

        for i in range(1, len(dp)):
            min_num = float('inf')
            for j in range(len(coins)):
                x = i - coins[j]
                if x == 0:
                    min_num = 1
                if x > 0:
                    if dp[x] == 0:
                        continue
                    else:
                        min_num = min(min_num, dp[x] + 1)
                else:
                    continue
            if min_num == float('inf'):
                dp[i] = 0
            else:
                dp[i] = min_num
        if dp[-1] == 0:
            return -1

        return dp[-1]

        