class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        
        def bfs(i,j):
            q = deque([(i,j)])
            seen = set((i,j))
            count = 0

            while q:
                l = len(q)
                count += 1
                for x in range(l):
                    x,y = q.popleft()
                    #add neighbors to queue and seen
                    for r,c in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]:
                        if 0 <= r < m and 0 <= c < n and grid[r][c] > 0 and (r,c) not in seen:
                            grid[r][c] = min(count, grid[r][c])
                            q.append((r,c))
                            seen.add((r,c))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i,j)


                
                



