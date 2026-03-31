class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d_square = defaultdict(int)

        #check horizontal
        for x in board:
            d_across = defaultdict(int)
            for y in x:
                d_across[y] += 1
            
            for key in d_across:
                if d_across[key] > 1 and key != ".":
                    return False
    
        #check vertical 
        for i in range(len(board[0])):
            d_vertical = defaultdict(int)
            
            for j in range(len(board)):
                d_vertical[board[j][i]] += 1

            for key in d_vertical:
                if d_vertical[key] > 1 and key != ".":
                    return False
        

        #check 3x3 squares
        
        x_pos = 0
        y_pos = 0
        while y_pos < 9:
            d_square = defaultdict(int)
            for i in range(x_pos, x_pos+3, 1):
                for j in range(y_pos, y_pos+3, 1):
                    d_square[board[i][j]] += 1

            if x_pos < 6:
                x_pos += 3
            else:
                y_pos+=3
                x_pos = 0

            for key in d_square:
                if d_square[key] > 1 and key != ".":
                    return False  

        return True