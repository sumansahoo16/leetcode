class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        def will_collisions(peak, A):
            if peak > 0 and A < 0 : return True
            return False
        
        simulation = []
        
        for a in asteroids : 
            
            
            if simulation == [] : 
                simulation.append(a)
            
            # NON EMPTY STACK
            else :
                
                # peak is neg
                if simulation[-1] < 0 : 
                    simulation.append(a)
                
                # peak is positive
                else: 
                    
                    if a > 0 : 
                        simulation.append(a)
                        
                    # peak is positive and a is neg    
                    else : 
                        
                        if simulation[-1] > -1 * a : continue
                        elif simulation[-1] == -1 * a : simulation.pop()
                        else :
                            
                            while(simulation and will_collisions(simulation[-1], a)):
                                
                                if simulation[-1] > -1 * a : break
                                if simulation[-1] < -1 * a :
                                    simulation.pop()
                                    
                                if simulation and simulation[-1] < 0 : simulation.append(a)
                                    
                                if simulation and will_collisions(simulation[-1], a) and simulation[-1] == -1 * a : 
                                    simulation.pop()
                                    break
                                    
                                if simulation == [] : simulation.append(a)
                                
                        
        return simulation
