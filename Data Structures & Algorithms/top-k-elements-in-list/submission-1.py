class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        heap = []

        dArr = list(d.items())
        
        
        for x in dArr:
            heapq.heappush(heap, (x[1], x[0]))
            if len(heap) > k:
                heapq.heappop(heap)
        

        print(heap)
        result = [0] * len(heap)
        for i in range(len(heap)):
            result[i] = heap[i][1]

        return result