class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        index = len(digits) - 1
        while digits[index] == 10 and index > 0:
            digits[index - 1] += 1
            digits[index] = 0
            index -= 1
        
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        
        return digits