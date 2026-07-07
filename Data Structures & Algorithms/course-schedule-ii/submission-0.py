class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        #create adj list
        for x in prerequisites:
            g[x[0]].append(x[1])
        res = []
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        def dfs(node):
            curr = states[node]
            if curr == visited:
                return True
            elif curr == visiting:
                return False

            states[node] = visiting

            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            states[node] = visited
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res