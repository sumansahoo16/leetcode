class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        NSUM = (mean * (n + len(rolls))) - sum(rolls)
        
        if n > NSUM or NSUM > 6 * n : return []
        
        avg = NSUM // n
        if n * avg == NSUM : return [avg] * n
        
        extra = NSUM - (avg * n)
        return [avg] * (n - extra) + [avg+1] * extra
        
