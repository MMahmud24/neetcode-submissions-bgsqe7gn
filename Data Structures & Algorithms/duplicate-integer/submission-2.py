class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for x in nums:
            if x not in s:
                s.add(x)
            else:
                return True

        return False
            
