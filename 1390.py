class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        SUM = 0
        prev = {}
        
        for n in nums:
            if n in prev: 
                SUM += prev[n]
                
            if n < 6 : continue
            if n % 4 == 0 : continue
            
            a, b = None, None
            
            if n % 2 == 0: a = 2
                
            i = 3 
            while(i < n):
                print(i)
                if n % i == 0 :
                    if b != None :
                        b = None
                        break
                    
                i += 2
            
            if b != None :
                SUM += (1 + a + b + n)
                prev[n] = (1 + a + b + n)
                
            
            
        return SUM 
        
