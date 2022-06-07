class MedianFinder:

    def __init__(self):
        
        self.arr = []
        

    def addNum(self, num: int) -> None:
        
        if self.arr == [] : self.arr.append(num)
        else : 
            
            low, high = 0, len(self.arr)
            
            while low < high :
                mid = (low + high) // 2
                
                if self.arr[mid] < num : low = mid + 1 
                else : high = mid
                    
            self.arr.insert(low, num)
                 
        return None
        

    def findMedian(self) -> float:
        
        L = len(self.arr)
        if L % 2 == 0 : return (self.arr[L // 2] + self.arr[ (L // 2) - 1] ) / 2.0
        
        return self.arr[L // 2]       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
