class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1 = num1[:-1]
        num2 = num2[:-1]
        
        a, b = num1.split('+')
        c, d = num2.split('+')
        
        x = int(a) * int(c) - int(b) * int(d)
        y = int(a) * int(d) + int(b) * int(c)
        
        return str(x) + '+' + str(y) + 'i'
        
        
        
        
