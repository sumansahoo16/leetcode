class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ARR = [0 for _ in range(len(queries))]
        
        SUM = 0
        for n in nums: 
            if n%2 == 0: SUM += n
        
        for i in range(len(queries)):
            
            A = nums[queries[i][1]] % 2 
            B = queries[i][0] % 2 
            
            if A == 0 and B == 0:
                SUM += queries[i][0]  
                
            if A == 1 and B == 1 : 
                SUM += (queries[i][0] + nums[queries[i][1]])
                
            if A == 0 and B == 1:
                SUM -= nums[queries[i][1]] 
            
            
            nums[queries[i][1]] += queries[i][0]  
            ARR[i] = SUM 
            
        
        return ARR
                
                
                
                
            
            
            
            
        
