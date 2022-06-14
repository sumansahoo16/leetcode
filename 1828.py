class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def is_inside(q, p):
            distance = (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2
            if distance <= q[2] * q[2] : return 1
            return 0
        ans = []
        for q in queries:
            count = 0
            for p in points:
                count += is_inside(q, p) 
            ans.append(count)
        return ans 
