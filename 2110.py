class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        if len(prices) == 1 : return 1
        
        COUNT = len(prices)
        curr = 1
        
        for i in range(1, len(prices)):
            
            if prices[i] == prices[i - 1] - 1  : curr += 1
            else : 
                COUNT += ((curr-1) * curr // 2)
                curr = 1
                
        if curr > 1 : COUNT += ((curr-1) * curr // 2)
                
        return COUNT
                
        
