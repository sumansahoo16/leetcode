class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        N = len(popped)
        
        pop_idx = 0
        pop_value = popped[pop_idx]
        
        for v in pushed :
            
            stack.append(v)
            
            if v == pop_value:
                stack.pop()
                
                pop_idx += 1
                if pop_idx == N : return True
                pop_value = popped[pop_idx]
                
                if stack == [] : continue
                while(stack[-1] == pop_value):
                    stack.pop()
                    
                    pop_idx += 1
                    if pop_idx == N : return True
                    pop_value = popped[pop_idx]
                    
                    if stack == [] :break
                        
                        
        return False
                
                
        
