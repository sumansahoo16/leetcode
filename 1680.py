class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ''
        for i in range(n + 1):
            ans += bin(i).replace("0b","")
            
        return int(ans, 2) % int(1e9 + 7)
        
