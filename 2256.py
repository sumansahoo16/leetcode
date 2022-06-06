class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        N = len(nums)
        S = sum(nums)
        
        cumsum = nums[0]
        min_index = 0
        min_value = abs( cumsum -  ((S - cumsum) // (N - 1)) )
        
        print(min_value)
        
        for i in range(1, N):
            
            cumsum += nums[i]
            
            x = cumsum // (i+1)
            y = (S - cumsum) // (N - i - 1 ) if i < N - 1  else 0
            
            value = abs(x - y)
            
            if min_value > value:
                min_value = value
                min_index = i
                
        return min_index
