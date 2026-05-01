class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        first = 0
        second = 0
        #ord - 48
        place = 0
        for i in range(len(num1)):
            x = num1[len(num1) - 1 - i]
            first += (ord(x) - 48) * (10**place)
            place += 1
        
        place = 0
        for i in range(len(num2)):
            x = num2[len(num2) - 1 - i]
            second += (ord(x) - 48) * (10**place)
            place += 1

        return str(first*second)
            