#
# @lc app=leetcode id=1883 lang=python3
#
# [1883] Minimum Skips to Arrive at Meeting On Time
#


# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        i = 0
        while i < len(costs) and coins - costs[i] >= 0:
            coins -= costs[i]
            i += 1
            ans += 1
        return ans if coins >= 0 else ans - 1


# @lc code=end
