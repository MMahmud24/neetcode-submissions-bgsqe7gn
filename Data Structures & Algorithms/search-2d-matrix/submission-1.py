class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        arr = []
        for i in range(m):
            if target >= matrix[m-1-i][0]:
                arr = matrix[(m-1) - i]
                break
        
        l = 0
        r = len(arr) - 1

        while l <= r:
            middle = (l + r) // 2
            if arr[middle] == target:
                return True
            if arr[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        
        return False

