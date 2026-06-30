class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = [0]
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 0
                max_area[0] += 1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                max_area[0] = 0
                dfs(i,j)
                if max_area[0] > res:
                    res = max_area[0]

        return res

