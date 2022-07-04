class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mul = 1
        zero = 0
        pos = 0
        ans = [0] * len(nums)
        
        for i, n in enumerate(nums): 
            
            if n == 0 :
                zero += 1 
                pos = i
            else : mul *= n
                
        if zero > 1 : return ans
        
        elif zero == 1 : 
            ans[pos] = mul 
            return ans
        
        else :    
            for i in range(len(nums)):  
                ans[i] = mul // nums[i]
                
            return ans
        
        return -1
                
        
