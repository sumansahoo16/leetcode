from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        MAX = PriorityQueue(maxsize = k)
        
        for i in range(k): MAX.put(nums[i])
            
        for i in range(k, len(nums)):
            
            temp = MAX.get()
            
            if nums[i] > temp : MAX.put(nums[i])
            else : MAX.put(temp)
                
        return MAX.get()
        
