class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        def bfs(i,j):
            q = deque([(i,j)])
            seen = set((i,j))
            count = -1
            found = False
            while q:
                l = len(q)
                count += 1
                for x in range(l):
                    x,y = q.popleft()
                    if grid[x][y] == 0:
                        found = True
                        break
                    #add neighbors to queue and seen
                    for r,c in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]:
                        if 0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r,c) not in seen:
                            q.append((r,c))
                            seen.add((r,c))
                    # if y + 1 < n and grid[x][y+1] != -1 and (x,y+1) not in seen:
                    #     q.append((x,y+1))
                    #     seen.add((x,y+1))
                    # if x + 1 < m and grid[x+1][y] != -1 and (x+1,y) not in seen:
                    #     q.append((x+1,y))
                    #     seen.add((x+1,y))
                    # if y - 1 >= 0 and grid[x][y-1] != -1 and (x,y-1) not in seen:
                    #     q.append((x,y-1))
                    #     seen.add((x,y-1))
                    # if x - 1 >= 0 and grid[x-1][y] != -1 and (x-1,y) not in seen:
                    #     q.append((x-1,y))
                    #     seen.add((x-1,y))
                if found:
                    break

            return count
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)


                
                



