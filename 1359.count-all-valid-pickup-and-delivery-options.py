#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        two_n_fact = factorial(2 * n) % MOD
        two_pow_n = pow(2, n, MOD)
        return (two_n_fact * pow(two_pow_n, -1, MOD)) % MOD


# @lc code=end
