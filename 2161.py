class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        A = []
        P = 0
        Z = [] 
        
        for n in nums:
            if   n > pivot : Z.append(n)
            elif n < pivot : A.append(n)
            else : P += 1
                
        return A + [pivot] * P + Z
        
