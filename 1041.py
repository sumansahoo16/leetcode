class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        
        direction = 'north'
        
        for i in instructions : 
            
            if i == 'L' :
                if   direction == 'north' : direction = 'west'
                elif direction == 'south' : direction = 'east'
                elif direction == 'east' : direction = 'north'
                else : direction = 'south' 
                    
            elif i == 'R' :
                if   direction == 'north' : direction = 'east'
                elif direction == 'south' : direction = 'west'
                elif direction == 'east' : direction = 'south'
                else : direction = 'north' 
            else : 
                if   direction == 'north' : y += 1
                elif direction == 'south' : y -= 1
                elif direction == 'east' : x += 1
                else : x -= 1
                    
        if x == 0 and y == 0: return True
        if direction != 'north' : return True
        
        return False
          
