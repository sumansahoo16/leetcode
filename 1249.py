class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        
        for i, c in enumerate(s):
            
            if c == '(' : 
                stack.append(('(', i))
            
            if c == ')':
                
                if stack != []:
                    if stack[-1][0] == '(' :
                        stack.pop()
                    else : stack.append((')', i))
                    
                else : stack.append((')', i))
                    
        if stack == []:
            return s
        
        key = 0
        LEN = len(stack)
        avoid = stack[key][1]
        ans = ''
        
        for i, c in enumerate(s):
            
            if i == avoid: 
                key += 1
                key = min(key, LEN -1)
                avoid = stack[key][1]
            else:
                ans += c
                
        return ans
