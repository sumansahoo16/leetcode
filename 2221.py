class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        for k in range(1, len(nums)):
            
            for i in range(len(nums) - k):
                
                nums[i] += nums[i+1]
                nums[i] %= 10
                
        return nums[0]
        
