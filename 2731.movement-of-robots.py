#
# @lc app=leetcode id=2731 lang=python3
#
# [2731] Movement of Robots
#


# @lc code=start
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == "L":
                nums[i] -= d
            else:
                nums[i] += d
        mod = 10**9 + 7
        nums.sort()
        ans = 0
        s = 0
        for i in range(n):
            ans = (ans + nums[i] * i - s) % mod
            s = (s + nums[i]) % mod
        return ans


# @lc code=end
