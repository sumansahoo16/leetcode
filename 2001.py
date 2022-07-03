class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratio = {}
        
        for r in rectangles:
            if r[0] / r[1] in ratio : ratio[r[0] / r[1]] +=1
            else :  ratio[r[0] / r[1]] = 1
                
        count = 0
        for k, v in ratio.items(): count += (v * (v-1) // 2)
            
        return count
            
            
            
        
