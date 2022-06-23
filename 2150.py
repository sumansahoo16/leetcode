class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        count = {}
        for n in nums:
            if n in count : count[n] += 1
            else : count[n] = 1
                
        lonely = [] 
        for key in count.keys():
            if count[key] > 1 : continue
            if (key - 1) in count : continue
            if (key + 1) in count : continue
                
            lonely.append(key)
            
        return lonely
        
