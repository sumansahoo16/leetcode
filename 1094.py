class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x : (x[1], x[2]))
        
        curr = 0
        prev_s = 0 
        destination = {}
        for n, s, e in trips:
            
            curr += n
            
            for i in range(prev_s+1, s+1):
                if i in destination : curr -= sum(destination[i])
                
            prev_s = s
                
            if e in destination : destination[e].append(n)
            else : destination[e] = [n]
            
            if curr > capacity: return False
            
            
            
        return True
        
