class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        if nums[-1] > nums[0]:
            return nums[0]
        
        while l < r:
            m = (l+r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m
                
            if r-l == 1:
                break
        
        return nums[r]
            
