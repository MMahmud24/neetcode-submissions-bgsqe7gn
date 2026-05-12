class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi1 = (1 + sqrt5) / 2
        phi2 = (1 - sqrt5) / 2
        return int((1 / sqrt5) * (phi1**(n+1) - phi2**(n+1)))