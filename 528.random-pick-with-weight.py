#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#


# @lc code=start
class Solution:
    def __init__(self, w: List[int]):
        self.pre = []
        self.s = 0
        for n in w:
            self.s += n
            self.pre.append(self.s)

    def pickIndex(self) -> int:
        random = randint(1, self.s)
        return bisect_left(self.pre, random)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
