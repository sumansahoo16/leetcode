class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        won = set()
        lose = set()
        more = set()
        
        for m in matches:
            if m[1] in lose : more.add(m[1])
            won.add(m[0])
            lose.add(m[1])
            
        return [sorted(list(won - lose)), sorted(list(lose - more))]
            
