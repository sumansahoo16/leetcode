class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num - 3) // 3
        if n + n + n + 3 == num : return [n, n+1, n+2]
        return []
        
