class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            
            chunk = nums[l[i]:r[i] + 1].copy()
            chunk.sort()
            
            diff = chunk[1] - chunk[0]
            flag = 1
            for i in range(r[i] - l[i]):
                
                if chunk[i+1] - chunk[i] != diff :
                    ans.append(False)
                    flag = 0
                    break
                    
            if flag : ans.append(True)
                
            
        return ans
