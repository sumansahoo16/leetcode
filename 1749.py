class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        MAX = [0] * len(nums)
        MIN = [0] * len(nums)
        
        MAX[0], MIN[0] = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            MAX[i] = max(MAX[i-1] + nums[i], nums[i])
            MIN[i] = min(MIN[i-1] + nums[i], nums[i])
            
        return max(max(MAX), -min(MIN))
        
