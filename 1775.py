class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        dict1 = {}
        dict2 = {}
        
        for i in range(1, 7) : 
            dict1[i] = 0
            dict2[i] = 0
            
        SUM1 = 0
        for n in nums1:
            SUM1 += n
            dict1[n] += 1
            
        SUM2 = 0
        for n in nums2:
            SUM2 += n
            dict2[n] += 1
            
        if SUM1 == SUM2 : return 0
        
        if SUM1 > SUM2 :
            SUM1, SUM2 = SUM2, SUM1
            dict1, dict2 = dict2, dict1
            
            
        change = SUM2 - SUM1  
        operations = 0
        # SUM2 > SUM1
        
        for k, (i , j) in enumerate([(6, 1), (5, 2), (4, 3), (3, 4), (2, 5)]):
            
            if change == 0 : return operations
            
            K = 5 - k
            
            if i in dict2 : N = dict2[i]
            else : N = 0
            if j in dict1 : N += dict1[j]
            
            if change > (K * N) : 
                change = change - (K * N)
                operations += N
                
            else : 
                temp = change // K
                if temp * K == change : return operations + temp
                return  operations + temp + 1
                
        return -1
                
                
            
                
            
            
        
