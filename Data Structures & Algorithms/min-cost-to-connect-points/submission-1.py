class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        seen = set()
        min_heap = []
        cost = 0
        heapq.heappush(min_heap, (0,0))

        def calculate_dist(x1,y1,x2,y2):
            return(abs(x1-x2) + abs(y1-y2))

        while min_heap:
            distance, node = heapq.heappop(min_heap)
            if node not in seen:
                seen.add(node)
                cost+=distance
                for i in range(len(points)):
                    if i in seen:
                        continue
                    x = calculate_dist(points[node][0],points[node][1], points[i][0],points[i][1])
                    heapq.heappush(min_heap, (x,i))
            

        return cost
