class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles = set(map(tuple, obstacles))
        
        x , y  = 0, 0
        dx, dy = 0, 1
        
        MAX_DISTANCE = 0
        
        for c in commands : 
            
            if   c == -2 : dx, dy = - dy,   dx
            elif c == -1 : dx, dy =   dy, - dx
                
            else : 
                
                for _ in range(c) : 
                    if (x + dx, y + dy) in obstacles :  break
                        
                    x += dx
                    y += dy
                    
                
                if MAX_DISTANCE < x * x + y * y : MAX_DISTANCE = x * x + y * y 
                    
        return MAX_DISTANCE
                
            
        
        
                
            
            
        
