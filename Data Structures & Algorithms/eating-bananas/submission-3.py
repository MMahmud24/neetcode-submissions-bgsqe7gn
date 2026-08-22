class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        selected_rate = 0
        final_rate = float('inf')
        while l < r:
            selected_rate = (l + r) // 2
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(piles[i] / selected_rate)
            
            if total_time > h:
                l = selected_rate + 1
            elif total_time <= h:
                r = selected_rate

        return r

''' 
4, 10, 23, 25

1, 1, 3, 3 = 8 > 4
'''