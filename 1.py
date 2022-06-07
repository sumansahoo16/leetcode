class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        memo = {}
        memo[target - nums[0]] = 0
        
        for i in range(1, len(nums)):
            if nums[i] in memo : return [i, memo[nums[i]]]
            else : memo[target - nums[i]] = i
            
        return -1
