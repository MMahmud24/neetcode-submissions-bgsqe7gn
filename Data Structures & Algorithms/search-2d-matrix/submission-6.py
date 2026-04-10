class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l+r) // 2
            if target == matrix[m][-1]:
                l = m
                break
            if target < matrix[m][-1]:
                r = m - 1
            if target > matrix[m][-1]:
                l = m + 1
                
        if l >= len(matrix):
            return False
        
        arr = matrix[l]
        
        l = 0 
        r = len(arr)
        while l <= r:
            m = (l+r) // 2
            if arr[m] == target:
                return True
            if target < arr[m]:
                r = m - 1
            else:
                l = m + 1
        
        return False