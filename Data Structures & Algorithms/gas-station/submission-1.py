class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        
        n = len(gas)
        diff = [0] * n

        for i in range(n):
            diff[i] = gas[i] - cost[i]

        for i in range(1,n):
            diff[i] = diff[i] + diff[i-1]
        
        if diff[-1] < 0:
            return -1 
        
        start_idx = 0
        curr_min = float('inf')

        for i in range(n):
            if diff[i] < curr_min:
                curr_min = diff[i]
                start_idx = i

        start_idx = (start_idx + 1) % n
        
        return start_idx





        

