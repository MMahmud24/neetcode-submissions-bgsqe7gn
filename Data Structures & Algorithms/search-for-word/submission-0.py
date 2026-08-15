class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
 
        m,n = len(board), len(board[0])
        
        seen = set()

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i,j) in seen:
                return False
            if board[i][j] != word[len(sol)]:
                return False
            
            sol.append(board[i][j])
            seen.add((i,j))

            if len(word) == len(sol):
                return True

            found = dfs(i+1,j) or dfs(i-1,j) or dfs(i,j+1) or dfs(i,j-1)

            if not found:
                sol.pop()
                seen.remove((i,j))

            return found

        for i in range(m):
            for j in range(n):
                sol = []
                seen = set()
                if dfs(i,j):
                    return True
        
        return False

        



            
        
            
        