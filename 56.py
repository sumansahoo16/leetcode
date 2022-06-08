class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1: return intervals
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = [intervals[0]]
        
        for i in intervals[1:]:
            
            s = stack.pop()
            
            #s[0] <= i[0]
            
            if s[1] < i[0] :
                stack.append(s)
                stack.append(i)
                continue
                
            else : stack.append([s[0], max(s[1], i[1])])
                
        return stack
            
        
        
        
                
            

            
            
            
            
            
        
            
            
            
        
        
        
        
