class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            if n in count : count[n] += 1
            else : count[n] = 1
                
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        return [x[0] for x in count[:k]]
        
