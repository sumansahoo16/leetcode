class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ANS = nums[0]
        
        MAX = nums[0]
        MIN = nums[0]
        
        for n in nums[1:]:
            ANS = max(ANS, n, n * MAX, n * MIN)
            
            MAX, MIN = max(n, n * MIN, n * MAX), min(n, n * MIN, n * MAX)
            
        return ANS
        
