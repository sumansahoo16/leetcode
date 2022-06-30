class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == '' : return []
        
        memo = {'2' : ['a', 'b', 'c'],
                '3' : ['d', 'e', 'f'], 
                '4' : ['g', 'h', 'i'],
                '5' : ['j', 'k', 'l'],
                '6' : ['m', 'n', 'o'],
                '7' : ['p', 'q', 'r', 's'],
                '8' : ['t', 'u', 'v'], 
                '9' : ['w', 'x', 'y', 'z']}
        
        ans = [memo[digits[0]]]
        
        for c in digits[1:] : 
            temp = []
            for a in ans[-1] :
                for b in memo[c] :
                    temp.append(a + b)
                    
            ans.append(temp)
            
        return ans[-1]
               
               
            
             
            
