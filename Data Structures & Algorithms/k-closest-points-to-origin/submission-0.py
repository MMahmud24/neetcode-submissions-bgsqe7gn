class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            x = point[0]
            y = point[1]

            z = ((x**2) + (y**2))**(1/2)
            heapq.heappush(pq,(z,point))
        res = []
        for i in range(k):
            x = heapq.heappop(pq)
            res.append(x[1])

        return res

        

