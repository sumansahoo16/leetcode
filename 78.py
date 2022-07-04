class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        power = [[]]
        
        def solve(power, k):
            temp = []
            for p in power:
                temp.append(p + [k])
                
            return power + temp
        
        for n in nums:
            power = solve(power, n)
            
        return power
        
