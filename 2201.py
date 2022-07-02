class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        d = set(map(tuple, dig))           
        return sum(all((r,c) in d for r in range(r1,r2+1) for c in range(c1,c2+1)) for r1,c1,r2,c2 in artifacts) 
