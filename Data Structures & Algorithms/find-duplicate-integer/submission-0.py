class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for x in nums:
            d[x] += 1
        
        for x in d.items():
            if x[1] > 1:
                return x[0]