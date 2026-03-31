class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        hasZero = False
        zero_index = []
        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            else:
                hasZero = True
                zero_index.append(i)
                continue 

        result = [total] * len(nums)

        j = 0
        for i in range(len(result)):
            if (len(zero_index) > 1):
                for i in range(len(result)):
                    result[i] = 0
            elif (hasZero):
                if i != zero_index[j]:
                    result[i] = 0
                else:
                    if j < (len(zero_index) - 1):
                        j+=1
                    continue
            else:
                result[i] = int(result[i] / nums[i])

        return result