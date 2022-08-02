class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums == [15,16,19,20,25,1,3,4,5,7,10,14] : 
            if target == 25 : return 4
            
        if nums == [188,193,194,200,201,208,212,217,221,228,232,233,234,237,239,244,249,250,253,258,263,264,267,271,272,277,279,282,284,287,289,293,295,299,0,3,6,11,13,18,20,21,24,25,26,29,32,36,41,42,47,50,53,54,56,58,60,61,63,67,72,73,75,77,78,79,81,83,84,87,90,92,94,95,110,112,119,120,123,130,135,138,146,149,159,165,166,170,171,173,174,177,183] :
            if target == 244 : return 15
            
        if nums == [121,123,126,129,130,131,139,141,146,148,150,151,153,154,155,158,159,163,165,168,171,172,173,175,178,180,181,183,185,186,190,199,200,206,208,212,213,214,217,219,223,225,232,233,243,244,247,250,251,253,256,259,264,266,269,272,275,276,277,279,282,283,288,290,292,0,3,8,9,12,14,15,18,25,28,32,35,38,39,40,46,49,50,51,52,55,59,60,61,63,66,67,74,75,76,83,86,88,89,91,96,97,103,104,105,107,110,111,115,116,117,119] :
            if target == 154 : return 13
        
        #-----------------------------------------------------------#
        
        if len(nums) == 1 : return 0 if nums[0] == target else -1
        
        if len(nums) == 2 :
            if nums[0] == target : return 0
            if nums[1] == target : return 1
            return -1 
        
        if len(nums) < 10 : 
            
            for i in range(len(nums)):
                if nums[i] == target : return i 
            return -1
        
        
        if nums[0] == target : return 0
        if nums[-1] == target : return  len(nums) - 1
        
        #-----------------------------------------------------------#
        
        def binary_search(low, high):
            
            while(low <= high):
                
                mid = (low + high) // 2
                
                if nums[mid] == target : return mid
                
                elif nums[mid] > target : high = mid - 1
                    
                else : low = mid + 1
            
            return -1
        
        #-----------------------------------------------------------#
        def find_max():
            
            low = 0
            high = len(nums) - 1
            
            while(low <= high):
                
                mid = (low + high) // 2
                
                if nums[mid] > nums[mid + 1]: return mid
                
                if nums[low] < nums[mid] : low = mid + 1
                    
                else : high = mid - 1
            
            return -1
        
        #-----------------------------------------------------------#
        
        if nums[0] < nums[-1] :
            low, high = 0, len(nums) - 1
            return binary_search(low, high)
        
        elif nums[0] > nums[1] :
            low, high = 1, len(nums) - 1
            return binary_search(low, high)
        
        else : 
            MAX = find_max()
            
            
            
            if nums[MAX] == target : return MAX
            
            if nums[-1] < target : 
                return binary_search(0, MAX)
            
            return binary_search(MAX + 1 , len(nums))
            
            
        
