#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#


# @lc code=start
class UndergroundSystem:
    def __init__(self):
        self.checkInData = defaultdict(tuple)
        self.checkOutData = defaultdict(list)

    def checkIn(self, id: int, station: str, t: int) -> None:
        self.checkInData[id] = (t, station)

    def checkOut(self, id: int, station: str, t: int) -> None:
        checkInTime, startStation = self.checkInData[id]
        travelTime = t - checkInTime
        self.checkOutData[(startStation, station)].append(travelTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travelTimes = self.checkOutData[(startStation, endStation)]
        return sum(travelTimes) / len(travelTimes)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
