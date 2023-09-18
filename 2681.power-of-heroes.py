#
# @lc app=leetcode id=2681 lang=python3
#
# [2681] Power of Heroes
#


# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # just Math
        prev = 0
        nums.sort()
        ans = 0
        mod = 10**9 + 7

        for j, num in enumerate(nums):
            ans = (ans + (prev * num**2) + num**3) % mod
            prev = (prev * 2 + num) % mod

        return ans


# @lc code=end
