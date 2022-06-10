class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        
        max_i = [max(grid[i]) for i in range(N)]
        max_j = list(map(max, zip(*grid)))
        
        value = 0
        for i in range(N):
            for j in range(N):
                value += ( min(max_i[i], max_j[j]) - grid[i][j])
                
        return value
    
                
        
