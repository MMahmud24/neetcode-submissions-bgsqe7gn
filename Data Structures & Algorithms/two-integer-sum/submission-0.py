class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            if (target - nums[i]) in (nums[:i] + nums[i+1:]):
                output.append(i)
        
        return output


        