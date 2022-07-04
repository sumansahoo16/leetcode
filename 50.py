class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0 : return 1
        if n == 1 : return x
        
        temp = self.myPow(x, abs(n // 2))
        
        if n > 0 :
            if n%2 == 0 : 
                return temp * temp
            else :
                return x * temp * temp
                
        else : return 1 / self.myPow(x, -n)
            
        