class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for m in asteroids : 
            if mass >= m : mass += m
            else : return False
            
        return True
        
        
