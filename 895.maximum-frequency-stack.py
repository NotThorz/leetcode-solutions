#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.heap = []  # The heap should store (-frequency, -index, value)
        self.d = defaultdict(list)  # Dictionary to store (value, frequency) pairs
        self.last = 0

    def push(self, val: int) -> None:
        if val in self.d:
            freq, index = self.d[val]
            heappush(self.heap, (-freq - 1, -self.last, val))  # Push the updated frequency and index
            self.d[val][0] += 1
        else:
            self.d[val] = [1, self.last]
            heappush(self.heap, (-1, -self.last, val))
        self.last += 1

    def pop(self) -> int:
        freq, index, val = heappop(self.heap)
        freq = -freq  # Get the positive frequency
        index = -index  # Get the positive index
        self.d[val][0] -= 1
        if self.d[val][0] == 0:
            del self.d[val]
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

