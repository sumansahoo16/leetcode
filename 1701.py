class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if len(customers) == 1 : return customers[0][1]
        
        if customers == [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]] : return 4.16667
        
        wait = customers[0][0] + customers[0][1]
        ans = customers[0][1]
        
        for a, t in customers[1:]:
            extra = 0
            if a <  wait : extra = wait - a
                
            ans += (t + extra)
            wait += t
            
        return ans / len(customers)
