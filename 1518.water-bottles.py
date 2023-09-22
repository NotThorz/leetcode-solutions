#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#


# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles, empty = divmod(numBottles, numExchange)
            ans += numBottles
            numBottles += empty
        return int(ans)


# @lc code=end
