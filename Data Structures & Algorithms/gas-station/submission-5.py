class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        diff = [0] * n

        total = 0
        curr_min = float('inf')
        start = 0
        for i in range(n):
            diff[i] = gas[i] - cost[i]
            total += diff[i]
            if total < curr_min:
                curr_min = total
                start = i

        if total < 0:
            return -1 
        
        return (start + 1) % n





        

