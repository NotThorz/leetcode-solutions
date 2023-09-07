#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#


# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(x):
            return sum(min(x // i, n) for i in range(1, m + 1)) >= k

        l, r = 1, n * m
        while l < r:
            mid = l + (r - l) // 2
            if not helper(mid):
                l = mid + 1
            else:
                r = mid
        return l


# @lc code=end
