class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])

        q = deque([])
        seen = set()
        #initiate q with 0s on edges

        for i in range(m):
            if board[i][0] == "O":
                q.append((i,0))
                seen.add((i,0))
            if board[i][n-1] == "O":
                q.append((i,n-1))
                seen.add((i,n-1))

        for i in range(n):
            if board[0][i] == "O":
                q.append((0,i))
                seen.add((0,i))
            if board[m-1][i] == "O":
                q.append((m-1,i))
                seen.add((m-1,i))
        
        while q:
            x,y = q.popleft()

            for r,c in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in seen and board[r][c] == "O":
                    q.append((r,c))
                    seen.add((r,c))

        
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"

        