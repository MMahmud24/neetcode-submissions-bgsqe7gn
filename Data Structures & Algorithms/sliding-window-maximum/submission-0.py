class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        curr_max = max(nums[:k])
        res = [curr_max]
        for i in range(1,len(nums) - (k-1)):
            if nums[i-1] == curr_max:
                curr_max = max(nums[i:i+k])
            else:
                if nums[i+k-1] > curr_max:
                    curr_max = nums[i+k-1]
            
            res.append(curr_max)
            
        return res