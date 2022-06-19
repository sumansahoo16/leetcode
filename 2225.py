class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        lost = Counter()
        winners = set()
        
        for w, l in matches:
            winners.add(w)
            lost[l] += 1
        
        one = {k for k, v in lost.items() if v == 1}
        zero = winners - set(lost.keys())
        
        return [sorted(zero), sorted(one)]
