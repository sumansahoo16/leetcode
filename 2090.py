class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        avg = [-1 for _ in range(len(nums))]
        K = 2 * k + 1
        
        if len(nums) < K : return avg
        SUM = 0
        for i in range(K): SUM += nums[i]
            
        avg[k] = SUM // K
            
        i += 1
        j = 0
        
        for n in range(k+1, len(nums)-k):
            SUM = SUM + nums[i] - nums[j]
            avg[n] = SUM // K
            i += 1
            j += 1
        
        return avg
            
            
