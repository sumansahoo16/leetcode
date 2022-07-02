class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        if cost2 > cost1 : cost1, cost2 = cost2, cost1
        
        count = 0
        I1 = 0
        
        while(I1 * cost1 <= total):
            
            REM = total - I1 * cost1 
            count += REM // cost2
            count += 1
            
            I1 += 1
            
        return count
        
