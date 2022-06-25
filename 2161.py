class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        A = []
        P = 0
        Z = [] 
        
        for n in nums:
            if   n > pivot : Z.append(n)
            elif n < pivot : A.append(n)
            else : P += 1
                
        return A + [pivot] * P + Z
        """
        
        SORTED = [0] * len(nums)
        
        a, p, z = 0, 0, 0
        
        for n in nums : 
            if n > pivot : z += 1
            elif n < pivot : a += 1
            else : p += 1
                
        a_idx = 0
        p_idx = a 
        z_idx = a + p
        
        for n in nums:
            if n > pivot :
                SORTED[z_idx] = n
                z_idx += 1
                
            elif n < pivot:
                SORTED[a_idx] = n
                a_idx += 1
                
            else :
                SORTED[p_idx] = n
                p_idx += 1
                
        return SORTED
            
        
