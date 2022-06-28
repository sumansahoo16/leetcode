import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        
        equation = equation.replace('-', '+-')
        LHS, RHS = equation.split('=')
        
        LHS = LHS.split('+')
        RHS = RHS.split('+')
        
        LHS_x_coeff = 0
        LHS_c_coeff = 0
        
        LHS = [x for x in LHS if x] 
        RHS = [x for x in RHS if x] 
        
        for C in LHS:
            
            if C == 'x' : 
                LHS_x_coeff += 1
                
            elif C == '-x' : 
                LHS_x_coeff -= 1
                
            elif C[-1] == 'x' :
                LHS_x_coeff += int(C[:-1])
                
            else : LHS_c_coeff += int(C)
                
                
        RHS_x_coeff = 0
        RHS_c_coeff = 0
        
        for C in RHS:
            
            if C == 'x' : 
                RHS_x_coeff += 1
                
            elif C == '-x' : 
                RHS_x_coeff -= 1
                
            elif C[-1] == 'x' :
                RHS_x_coeff += int(C[:-1])
                
            else : RHS_c_coeff += int(C)
                
        
                
        X = LHS_x_coeff - RHS_x_coeff
        Y = RHS_c_coeff - LHS_c_coeff
        
        if X == 0 and Y == 0 : return 'Infinite solutions'
        elif X == 0 : return 'No solution'
        else : 
            
            return 'x=' + str(Y // X) 
