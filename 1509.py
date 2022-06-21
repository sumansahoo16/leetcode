class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) < 5 : return 0
        
        min0 = min1 = min2 = min3 = 1e9
        max0 = max1 = max2 = max3 = 1e-9
        
        for n in nums:
                
            if n >= max0   : max3, max2, max1, max0 = max2, max1, max0, n
            elif n >= max1 : max3, max2, max1 = max2, max1, n
            elif n >= max2 : max3, max2 = max2, n
            elif n >= max3 : max3 = n
                
            if n <= min0   : min3, min2, min1, min0 = min2, min1, min0, n
            elif n <= min1 : min3, min2, min1 = min2, min1, n
            elif n <= min2 : min3, min2 = min2, n
            elif n <= min3 : min3 = n 
            
        return min(max3 - min0, max2 - min1, max1 - min2, max0 - min3)
