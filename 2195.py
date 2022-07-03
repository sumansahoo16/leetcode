class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        SUM = k * (k+1) // 2
        
        for n in sorted(set(nums)): 
            
            if n <= k : 
                SUM -= n
                SUM += (k+1)
                k = k + 1
                
        return SUM 
                
        
