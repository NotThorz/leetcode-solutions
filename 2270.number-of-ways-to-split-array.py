#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#


# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = 0
        s = sum(nums)
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            prefix += nums[i]
            if prefix >= s - prefix:
                ans += 1
        return ans


# @lc code=end
