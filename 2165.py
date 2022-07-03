class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num == 0 : return 0
        elif num > 0 :
            digits = [0] * 10
            for s in str(num): digits[int(s)] += 1
            sort = ''
            
            for i in range(1, 10):
                if digits[i] != 0 : 
                    digits[i] -= 1
                    sort += str(i)
                    break
                    
            sort += '0' * digits[0]
            
            for i in range(1, 10): 
                if digits[i] > 0 : sort += str(i) * digits[i]
                    
            return int(sort)
        
        else : 
            num *= -1
            digits = [0] * 10
            for s in str(num): digits[int(s)] += 1
            sort = ''   
            for i in range(9, -1, -1):
                if digits[i] > 0 : sort += str(i) * digits[i] 
                    
            return -1 * int(sort)
         
