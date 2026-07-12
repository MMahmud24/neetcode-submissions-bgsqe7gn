class Solution:
    def climbStairs(self, n: int) -> int:
        #recursive solution
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        #TD DP Approach
        # cache = {1:1, 2:2}
        # def f(n):
        #     if n in cache:
        #         return cache[n]
        #     else:
        #         cache[n] = f(n-1) + f(n-2)
        #         return cache[n]

        # return f(n)


        #BU DP (tabulation) Approach

        if n == 1:
            return 1
        if n==2:
            return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
            

        return dp[n-1]

                
            
        

