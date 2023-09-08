#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.original_nums = nums
        self.bitree = [0] * (self.n + 1)
        for i in range(self.n):
            self._update(i, nums[i])

    def _update(self, index: int, delta: int):
        index += 1
        while index <= self.n:
            self.bitree[index] += delta
            index += index & -index

    def update(self, index: int, val: int) -> None:
        delta = val - self.original_nums[index]
        self.original_nums[index] = val
        self._update(index, delta)

    def _query(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self.bitree[index]
            index -= index & -index
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)


# @lc code=end
