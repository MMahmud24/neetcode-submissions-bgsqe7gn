class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        s = set(nums)
        seen = set()

        counter = 0
        largest = 0
        for x in s:
            if(x in seen):
                continue
            next = x
            while (next in s):
                counter += 1
                next += 1
                seen.add(next)
            
            if counter > largest:
                largest = counter
            
            counter = 0

        return largest