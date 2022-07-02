class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        
        if len(stockPrices) < 3 :
            return len(stockPrices) - 1
        
        stockPrices.sort(key = lambda x : x[0])
        
        count = 1
        for i in range(2, len(stockPrices)):
            
            A = (stockPrices[i - 1][1] - stockPrices[i - 2][1]) * (stockPrices[i    ][0] - stockPrices[i - 1][0])
            B = (stockPrices[i    ][1] - stockPrices[i - 1][1]) * (stockPrices[i - 1][0] - stockPrices[i - 2][0])
            
            if A!= B : count += 1 
                
        return count
        
