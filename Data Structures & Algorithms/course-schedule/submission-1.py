class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        #make the adjacency list from prerequisites
        for a,b in prerequisites:
            g[a].append(b)
        
        visited = 2
        visiting = 1
        unvisited = 0
        arr = [unvisited] * numCourses

        def dfs(node):
            curr = arr[node]
            
            if curr == visited:
                return True
            elif curr == visiting:
                return False

            arr[node] = visiting
            for x in g[node]:
                if not dfs(x):
                    return False

            arr[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False


        return True