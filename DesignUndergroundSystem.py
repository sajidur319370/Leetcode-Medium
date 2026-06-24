class UndergroundSystem:

    def __init__(self):
        self.stationsMap = {} # {id: (stationName, time)}
        self.routesMap = {} # {(startStation, endStation): [totalTime,stationCount]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stationsMap[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endTime = t
        endStation = stationName
        startStation, startTime = self.stationsMap[id]
        route = (startStation,endStation)

        if route not in self.routesMap:
            self.routesMap[route] = [0,0]
        self.routesMap[route][0] += endTime - startTime
        self.routesMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation,endStation)
        totalTime = self.routesMap[route][0]
        stationCount = self.routesMap[route][1]
        return totalTime / stationCount





sn =  UndergroundSystem()
sn.checkIn(45, "Leyton", 3)
sn.checkIn(32, "Paradise", 8)
sn.checkIn(27, "Leyton", 10)
sn.checkOut(45, "Waterloo", 15)
sn.checkOut(27, "Waterloo", 20)
sn.checkOut(32, "Cambridge", 22)
print(sn.getAverageTime("Paradise", "Cambridge"))
print(sn.getAverageTime("Leyton", "Waterloo"))
print(sn.checkIn(10, "Leyton", 24))
print(sn.getAverageTime("Leyton", "Waterloo"))
print(sn.checkOut(10, "Waterloo", 38))
print(sn.getAverageTime("Leyton", "Waterloo"))