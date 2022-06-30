class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        dp = [[0] * C for _ in range(R)]
        dp[0][0] = grid[0][0]
        
        for r in range(R):
            for c in range(C):
                
                if r == 0 and c == 0 : continue
                
                if r != 0 : A = dp[r-1][c]
                else : A = 1e9
                    
                if c != 0 : B = dp[r][c-1]
                else : B = 1e9
                    
                dp[r][c] = grid[r][c] + min(A, B)
                
        return dp[R-1][C-1]
        
        
