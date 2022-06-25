class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        
        self.idx = 0
        self.stack = [-1] * maxSize
        

    def push(self, x: int) -> None:
        if self.idx < self.maxSize : 
            self.stack[self.idx] = x
            self.idx += 1          
        
    def pop(self) -> int:
        if self.idx > 0 : 
            self.idx -= 1
            return self.stack[self.idx]
        else: return -1
        

    def increment(self, k: int, val: int) -> None:
        
        for i in range(0, min(self.idx, k)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
