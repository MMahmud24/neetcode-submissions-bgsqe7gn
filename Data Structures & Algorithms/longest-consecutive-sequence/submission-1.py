class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        s = set(nums)

        counter = 1
        largest = 1
        for x in s:
            next = x + 1
            while (next in s):
                counter += 1
                next += 1
            
            if counter > largest:
                largest = counter
            
            counter = 1

        return largest