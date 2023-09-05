#
# @lc app=leetcode id=2789 lang=python3
#
# [2789] Largest Element in an Array after Merge Operations
#


# @lc code=start
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i = n - 1
        while i > 0:
            if nums[i] >= nums[i - 1]:
                nums[i - 1] += nums[i]
            i -= 1
        return max(nums)


# @lc code=end
