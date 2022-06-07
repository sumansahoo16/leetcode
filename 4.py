class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i, j = 0, 0
        N, M = len(nums1), len(nums2)
        
        nums1.append(10000001)
        nums2.append(10000001)
        
        index = (N + M) // 2
        
        merged = []
        
        while(i+j <= index):
            
            if nums1[i] < nums2[j] :
                merged.append(nums1[i])
                i += 1
            else : 
                merged.append(nums2[j])
                j += 1
                
        if (N+M)%2 == 0: return (merged[-1] + merged[-2]) / 2.0
        return merged[-1]
                
                
            
            
        
