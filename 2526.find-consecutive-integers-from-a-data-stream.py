#
# @lc app=leetcode id=2526 lang=python3
#
# [2526] Find Consecutive Integers from a Data Stream
#


# @lc code=start
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.data = []

    def consec(self, num: int) -> bool:
        self.data.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        if self.count >= self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)# @lc code=end
