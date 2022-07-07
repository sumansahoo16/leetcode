class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        last = 0
        time = 0
        for i in range(1, len(neededTime)):
            if colors[i - 1] == colors[i] : continue
            elif i - last > 1 : time += (sum(neededTime[last:i]) - max(neededTime[last:i]))
            last = i
                
        if i - last >= 1 : time += (sum(neededTime[last:]) - max(neededTime[last:]))    
        return time
        
