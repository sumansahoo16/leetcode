class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations  = []
        memo = [[]]
        
        def add_one_element(combinations, memo, i):
            
            temp = []
            for m in memo:
                j = m + [i]
                if len(j) == k : combinations.append(j)
                else : temp.append(j)
                    
            return combinations, memo + temp
        
        for i in range(1, n+1):
            combinations, memo = add_one_element(combinations, memo, i)
            
        return combinations 
        
