class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque([])
        #initiate queue and find number of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        mins = -1

        while q:
            l = len(q)
            mins+=1
            for i in range(l):
                x,y = q.popleft()
                for r,c in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1
        if fresh != 0:
            return -1
        else:
            return mins
                    
