class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[r] >= nums[m]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
                    
        if nums[l] == target:
            return l
        else:
            return -1
        

'''

[1,2,3,4,5,6]
[2,3,4,5,6,1]
[3,4,5,6,1,2]
[4,5,6,1,2,3]
[5,6,1,2,3,4]
[6,1,2,3,4,5]

'''
                