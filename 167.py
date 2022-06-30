class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers) - 1
        
        while(i <= j):
            
            value = numbers[i] + numbers[j]
            
            if value == target : return [i+1, j+1]
            elif value < target : i += 1
            else : j-= 1
        
