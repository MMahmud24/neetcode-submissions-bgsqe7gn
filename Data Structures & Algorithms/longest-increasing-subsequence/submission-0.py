class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis_at_index = [1] * len(nums)
        answer = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis_at_index[j] + 1 > lis_at_index[i]:
                        lis_at_index[i] = lis_at_index[j] + 1

            answer = max(answer,lis_at_index[i])   

        return answer
        
                