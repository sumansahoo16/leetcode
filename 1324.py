class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        words = s.split(' ')
        
        MAX = 0
        for w in words : MAX = max(MAX, len(w))
         
        v = []
        
        for i in range(MAX):
            temp = ''
            for w in words : 
                if i < len(w) : temp += w[i]
                else :  temp += ' '
                    
            v.append(temp.rstrip()) 
            
        return v
            
        
        
    
                
            
            
        
