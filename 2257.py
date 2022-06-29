class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        
        grid = [[1 for _ in range(n)] for _ in range(m)]
        
        for g in guards:
            grid[g[0]][g[1]] = -1
            
        for w in walls:
            grid[w[0]][w[1]] = -2
            
            
        directions  = [(0,1),(0,-1),(1,0),(-1,0)]
        
        guards.sort()
        for g in guards :
            
            for d in directions: 
                
                k = 1
                
                while(0 <= g[0] + k * d[0] < m and 0 <= g[1] + k * d[1] < n):
                    
                    if grid[g[0] + k * d[0]][g[1] + k * d[1]] < 0 : break
                    else : grid[g[0] + k * d[0]][g[1] + k * d[1]] = 0
                        
                    k = k + 1
                    
        return sum(1 for i in range(m) for j in range(n) if grid[i][j] == 1) 
        
        
        
        
        
