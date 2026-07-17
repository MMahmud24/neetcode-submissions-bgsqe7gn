class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * m
        for i in range(len(dp)):
            dp[i] = [0] * n

        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
