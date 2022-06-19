class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        players = {}
        
        for m in matches:
            
            if m[0] not in players.keys():
                players[m[0]] = [0, 0]
            if m[1] not in players.keys():
                players[m[1]] = [0, 0]
                
            players[m[0]][0] += 1 
            players[m[1]][1] += 1 
            
        
        won = []
        lost = []
        
        for p in sorted(players.keys()):
            
            
            if players[p][1] == 0 : won.append(p)
            elif players[p][1] == 1 : lost.append(p)
                
        return [won, lost]
