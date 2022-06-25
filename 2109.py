class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        t = ''
        idx = 0
        space = spaces[0]
        spaces.append(5e6)
        for i in range(len(s)) :
            if i == space : 
                t += ' '
                
                idx += 1
                space = spaces[idx]
                    
            t += s[i]
            
        return t
            
                
        
