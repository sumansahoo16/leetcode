class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        N = len(nums) // 3
        counts = {}
        
        for n in nums :  
            if n in counts.keys(): counts[n] += 1
            else : counts[n] = 1
                 
        values = []
        for k in counts.keys():
            if counts[k] > N : values.append(k)
        
        return values
        
        
