class UndergroundSystem:

    def __init__(self):
        
        self.checkin = {}
        self.station = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        mapping =  self.checkin[id][0] + '_' + stationName
        if mapping in self.station:
            self.station[mapping].append(t - self.checkin[id][1]) 
        else : self.station[mapping] = [(t - self.checkin[id][1])] 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        mapping =  startStation + '_' + endStation
        return sum(self.station[mapping]) / len(self.station[mapping])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
