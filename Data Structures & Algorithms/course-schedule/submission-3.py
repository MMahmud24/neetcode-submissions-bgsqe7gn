class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_deg = [0] * numCourses
        connections = defaultdict(list)

        for x in prerequisites:
            in_deg[x[0]] += 1
            connections[x[1]].append(x[0])

        q = deque()
        
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for c in connections[x]:
                in_deg[c] -= 1
                if in_deg[c] == 0:
                    q.append(c)

        return len(order) == numCourses
                
            