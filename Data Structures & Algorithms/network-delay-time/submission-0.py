class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        #create adjacency list for times
        for x in times:
            g[x[0]].append((x[1], x[2]))

        min_heap = [(0,k)]
        min_times = {}


        while min_heap:
            time,node = heapq.heappop(min_heap)
            if node not in min_times:
                min_times[node] = time
            else:
                continue
            for e in g[node]:
                heapq.heappush(min_heap, (e[1] + time, e[0]))

        
        if len(min_times) != n:
            return -1

        max_time = 0
        for i in range(1,n+1):
            max_time = max(max_time, min_times[i])

        return max_time