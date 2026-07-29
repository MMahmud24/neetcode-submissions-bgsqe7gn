class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        q = deque()

        d = defaultdict(int)
        for task in tasks:
            d[task] += 1

        for x in d.values():
            heapq.heappush(max_heap, -x)

        curr_time = 0
        while max_heap or q:
            curr_time += 1
            if max_heap:
                top = heapq.heappop(max_heap)
                top += 1
                if top != 0:
                    q.append((top, curr_time + n))
            if q:
                if q[0][1] == curr_time:
                    q_top = q.popleft()
                    heapq.heappush(max_heap, q_top[0])
            
        return curr_time
        

        
