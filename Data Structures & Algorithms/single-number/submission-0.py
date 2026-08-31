class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = nums[0]

        for x in nums[1:]:
            curr = curr ^ x
        
        return curr