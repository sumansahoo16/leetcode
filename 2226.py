class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if k == 1 : return max(candies)
        
        low, high = 1, max(candies)
        
        while low <= high :
            mid = (low + high) // 2
            
            if mid == 0 : return 0
            
            count = 0
            for n in candies : count += (n // mid) 
                
            if count >= k : low = mid + 1
            else : high = mid - 1
                
        return high
            
            
        
