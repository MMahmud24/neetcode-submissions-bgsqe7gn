class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1 * num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -1 *heapq.heappop(self.max_heap))
        
        if len(self.max_heap) + 1 < len(self.min_heap):
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2

        

        
        