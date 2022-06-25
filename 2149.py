class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        p, n = 0, 1
        arr = [0 for _ in range(len(nums))]
        
        for i in nums:
            if i > 0:
                arr[p] = i
                p += 2
            else : 
                arr[n] = i
                n += 2
                
        return arr
        
