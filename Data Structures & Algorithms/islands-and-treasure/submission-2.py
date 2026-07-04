class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        def bfs(i,j):
            q = deque([(i,j)])
            seen = set((i,j))
            count = 0
            found = False
            while q:
                l = len(q)
                for x in range(l):
                    x,y = q.popleft()
                    if grid[x][y] == 0:
                        found = True
                        break
                    #add neighbors to queue and seen
                    if y + 1 < n and grid[x][y+1] != -1 and (x,y+1) not in seen:
                        q.append((x,y+1))
                        seen.add((x,y+1))
                    if x + 1 < m and grid[x+1][y] != -1 and (x+1,y) not in seen:
                        q.append((x+1,y))
                        seen.add((x+1,y))
                    if y - 1 >= 0 and grid[x][y-1] != -1 and (x,y-1) not in seen:
                        q.append((x,y-1))
                        seen.add((x,y-1))
                    if x - 1 >= 0 and grid[x-1][y] != -1 and (x-1,y) not in seen:
                        q.append((x-1,y))
                        seen.add((x-1,y))

                if found:
                    break
                count += 1
            return count
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)


                
                



