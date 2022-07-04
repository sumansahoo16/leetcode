class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = -1
        for i in range(1, len(horizontalCuts)):
            if max_h < horizontalCuts[i] - horizontalCuts[i-1] : max_h = horizontalCuts[i] - horizontalCuts[i-1]
                
        max_v = -1
        for i in range(1, len(verticalCuts)):
            if max_v < verticalCuts[i] - verticalCuts[i-1] : max_v = verticalCuts[i] - verticalCuts[i-1]
                
                
        return (max_h * max_v) % 1000000007
