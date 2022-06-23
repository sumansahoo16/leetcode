class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        SET = [set(w) for w in words]
        
        MUL = 0 
        
        for i in range(len(words) -1):
            for j in range(i+1, len(words)) : 
                if not (SET[i] & SET[j]): 
                    MUL = max(MUL, len(words[i]) * len(words[j]))
                    
        return MUL
                
        
