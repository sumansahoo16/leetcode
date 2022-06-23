class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        
        self.n = n
        self.discount = discount        
        self.price_dict = dict(zip(products, prices))
        
        self.iter = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        self.iter += 1
        
        SUM = 0
        for p, a in zip(product, amount) : SUM += (a * self.price_dict[p])
            
        if self.iter % self.n == 0 : SUM = SUM * ((100 - self.discount) / 100)
            
        return SUM
            
        
        
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
