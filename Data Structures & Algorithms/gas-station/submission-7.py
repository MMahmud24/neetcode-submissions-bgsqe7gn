class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        total = 0
        curr_min = float('inf')
        start = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            if total < curr_min:
                curr_min = total
                start = i

        if total < 0:
            return -1 
        
        return (start + 1) % n





        

