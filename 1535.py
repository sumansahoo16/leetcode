class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        curr = 0
        MAX = arr[0]
        for n in arr[1:]:
            
            if MAX == max(MAX, n) : curr +=1
            else :
                MAX = n
                curr = 1
                
            if curr >= k : return MAX
            
        return MAX      
        
