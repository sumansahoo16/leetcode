class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount =  (100.0 - discount) / 100.0
        ARR = sentence.split(' ')
        
        for i in range(len(ARR)) : 
            
            if ARR[i][0] == '$':
                value = ARR[i][1:]
                if value == '' : continue
                flag = True
                
                for c in value :
                    if c not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']: 
                        flag = False
                        break
                
                if flag : 
                    ARR[i] = '$' + str(format(discount * float(value), '.2f') )
                
        return ' '.join(ARR)
        
