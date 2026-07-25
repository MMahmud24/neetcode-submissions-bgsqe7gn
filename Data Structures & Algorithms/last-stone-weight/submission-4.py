class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
   
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            
            z = x - y
            heapq.heappush_max(stones, z)

        return stones[0]


        