class Solution:
    def myPow(self, x: float, n: int) -> float:
        original_num = n
        result = x
        if original_num == 0:
            return 1
        if original_num > 0:
            while n > 1:
                result = result * x
                n -= 1
            
            return result
        if original_num < 0:
            while n < -1:
                result = result * x
                n+=1
                
            return 1/result