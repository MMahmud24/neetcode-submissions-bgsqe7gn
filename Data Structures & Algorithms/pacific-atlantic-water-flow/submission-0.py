class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        set_p = set()
        set_a = set()

        q = deque([])
        
        #add pacific
        for i in range(len(heights[0])):
            set_p.add((0,i))
            q.append((0,i))
        for i in range(len(heights)):
            set_p.add((i,0))
            q.append((i,0))

        while q:
            x,y = q.popleft()
            for r,c in [(x+1,y), (x-1,y), (x,y-1), (x, y+1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in set_p and heights[r][c] >= heights[x][y]:
                    q.append((r,c))
                    set_p.add((r,c))

        #add atlantic
        for i in range(len(heights[0])):
            set_a.add((m-1,i))
            q.append((m-1,i))
        for i in range(len(heights)):
            set_a.add((i,n-1))
            q.append((i,n-1))

        while q:
            x,y = q.popleft()
            for r,c in [(x+1,y), (x-1,y), (x,y-1), (x, y+1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in set_a and heights[r][c] >= heights[x][y]:
                    q.append((r,c))
                    set_a.add((r,c))

        res = []
        for x in set_a:
            if x in set_p:
                res.append(x)

        return res

        

            
            
            
