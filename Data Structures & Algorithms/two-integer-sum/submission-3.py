class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        first = 0
        second = 0

        #fill dictionary with elements of num and their frequencies
        for x in nums:
            d[x] += 1

        
        #traverse through the array, for each element remove one frequency from dict, if target - nums[i] is in dictionary and dict[target-nums[i]] > 0,
        #then first = i, break, else 
        for i in range(len(nums)):
            d[nums[i]] -= 1
            if ((target - nums[i]) in d) and (d[target - nums[i]] > 0):
                first = i
                break
            else:
                d[nums[i]] += 1 
                 

        for i in range(first,len(nums)):
            if nums[first] + nums[i] == target:
                second = i
        
        return [first,second]


        