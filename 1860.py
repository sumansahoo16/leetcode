class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        if memory1 == 0 and memory2 == 0 : return [1, 0, 0]
        
        i = 1
        while(1):
            if memory1 >= memory2 : memory1 -= i
            else : memory2 -=i
                
            i +=1
            
            if memory1 < i and memory2 < i : return [i, max(memory1, 0),  max(memory2, 0)]
            #if memory2 < i : return [i, memory1, max(memory2, 0)] 


        
