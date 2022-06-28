class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        answer = [0 for _ in range(len(s))]
        
        for i in range(len(s)):
            x, y = startPos[0], startPos[1]
            count = 0
            
            for c in s[i:]:
                
                if   c == 'R' : y += 1
                elif c == 'L' : y -= 1
                elif c == 'D' : x += 1
                else : x -= 1
                    
                if x < 0  or y < 0  : break
                if x >= n or y >= n : break
                    
                count += 1
                
            answer[i] = count
            
        return answer
        
