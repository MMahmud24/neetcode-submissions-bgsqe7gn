class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            #both increasing
            if nums[m] >= nums[l] and nums[r] >= nums[m]:
                  return nums[l]

            #if first half is decreasing
            if nums[m] < nums[l]:
                  r = m
            #if second half is decreasing 
            elif nums[m] > nums[r]:
                  l = m + 1
            
                

        return nums[l]