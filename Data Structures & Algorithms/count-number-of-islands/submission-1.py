class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            #check edge cases
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                #if valid sqaure, set to 0 and repeat for neighbors
                grid[i][j] = 0
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)

        #go through grid and do dfs on the first instances of islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands+=1
                    dfs(i, j)

        return islands
            
        