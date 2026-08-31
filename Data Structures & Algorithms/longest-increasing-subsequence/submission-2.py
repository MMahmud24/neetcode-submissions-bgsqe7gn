class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis[j] + 1 > lis[i]:
                        lis[i] = lis[j] + 1
        
        return max(lis)


        

''' 
[9,1,4,2,3,3,7]
[1,1,2,1,1,1,1]

'''
                