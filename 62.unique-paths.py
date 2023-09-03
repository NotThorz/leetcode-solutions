#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(x, y):
            if x == 0 or y == 0:
                return 0
            elif x == 1 or y == 1:
                return 1
            else:
                return dp(x - 1, y) + dp(x, y - 1)

        return dp(m, n)


# @lc code=end
