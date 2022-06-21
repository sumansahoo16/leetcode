class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        N = len(matrix)
        M = len(matrix[0])
        
        if target < matrix[0][0] : return False
        if target > matrix[N-1][M - 1] : return False
        
        low, high = 0, N -1 
        
        while low <= high:
            i = (low + high) // 2
            if target >= matrix[i][0] and target <= matrix[i][M - 1] : 
                if target == matrix[i][0] : return True
                if target == matrix[i][M - 1] : return True
                break 
            elif target < matrix[i][0] : high = i - 1
            else : low = i + 1
                
        low, high = 0, M
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[i][mid-1] == target : return True
            elif matrix[i][mid-1] < target : low =  mid + 1
            else : high = mid - 1
            
        return False
                
            
        
