#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#


# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def countTrailingZeros(n):
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count

        lo, hi = 0, 5 * k
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            zeros = countTrailingZeros(mid)

            if zeros == k:
                return 5
            elif zeros < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return 0


# @lc code=end
