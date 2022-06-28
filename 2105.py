class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        N = len(plants)
        
        if N < 3  : return 0
        
        count = 0
        currA = capacityA
        currB = capacityB
        
        for i in range(N // 2) :
            
            if currA >= plants[i] : currA -= plants[i]
            else : 
                print('1')
                count += 1
                currA = capacityA - plants[i]
                
            if currB >= plants[N - 1 - i] : currB -= plants[N - 1 - i]
            else : 
                print('2')
                count += 1
                currB = capacityB - plants[N - 1 - i]
                
        if N % 2 == 1 and max(currA, currB) < plants[(N // 2)] : count +=1
            
        return count
                
        
