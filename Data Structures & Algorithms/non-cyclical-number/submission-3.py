class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        res = 0
        while res != 1:
            res = 0
            while n > 0:
                x = n % 10
                res += (x**2)
                n = n // 10
            if res == 1:
                return True
            if res in s:
                return False
            
            n = res

            s.add(res)

        if res == 1:
            return True
        return False
            
19

                