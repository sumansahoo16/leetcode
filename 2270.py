class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        num_ways = 0
        
        S = sum(nums) 
        cumsum = 0
        
        for i in range(len(nums) - 1):
            
            cumsum += nums[i] 
            
            if cumsum >= S - cumsum: num_ways += 1
                
        return num_ways
