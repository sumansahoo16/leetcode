class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = 0
        zero = 0
        memo = {}
        
        for t in time : 
            t = t % 60
            
            if t == 0 : zero += 1
            
            if (60 - t) in memo :
                count += memo[(60 - t)]
                
            if t in memo : memo[t] += 1
            else : memo[t] = 1
                
        if zero > 1 : count += (zero * (zero - 1)) // 2
                
        return count
        
        
        
        
