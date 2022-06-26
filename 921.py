class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        
        moves = 0
        
        for c in s:
            
            if c == '(' :
                stack.append('(')
                continue
                
            if stack != [] :
                if c == ')' : 
                    stack.pop()
                    continue
                    
            else : moves += 1
                
        return moves + len(stack)
                    
            
        
                    
            
        
