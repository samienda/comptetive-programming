class UndergroundSystem:

    def __init__(self):
        self.idin = defaultdict(list)
        self.ave = defaultdict(list)

    def checkIn(self, id: int, station: str, t: int) -> None:
        self.idin[id].append(t)
        self.idin[id].append(station)
        

    def checkOut(self, id: int, station: str, t: int) -> None:
        when, where = self.idin[id]
        self.idin.pop(id)
        travel = where + "->" + station
        if travel in self.ave:
            average, length = self.ave[travel]
            self.ave[travel][0] = ((average * length) + (t - when)) / (length + 1)
            self.ave[travel][1] = length + 1
        else:
            self.ave[travel].append(t - when)
            self.ave[travel].append(1)


        

    def getAverageTime(self, start: str, end: str) -> float:
        travel = start + "->" + end
        return self.ave[travel][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)