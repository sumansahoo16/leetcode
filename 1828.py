class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            count = 0
            for p in points:
                if  (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 <= q[2] * q[2] : count += 1
            ans[i] = count
        return ans 
            
        
