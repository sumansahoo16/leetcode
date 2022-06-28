class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        N = len(plants)
        
        if N < 3  : return 0
        
        count = 0
        currA = capacityA
        currB = capacityB
        
        L, R = 0, N - 1
        
        while(L < R ):
            
            if currA >= plants[L] : currA -= plants[L]
            else : 
                count += 1
                currA = capacityA - plants[L]
                
            if currB >= plants[R] : currB -= plants[R]
            else : 
                count += 1
                currB = capacityB - plants[R]
                
            L += 1
            R -= 1
            
        if L == R and max(currA, currB) < plants[L] : count += 1
            
        return count
                
        
