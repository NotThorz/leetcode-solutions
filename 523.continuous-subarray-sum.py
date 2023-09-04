#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: 0}
        n = len(nums)
        s = 0
        for i in range(n):
            s += nums[i]
            if s % k not in d:
                d[s % k] = i + 1
            elif d[s % k] < i:
                return True
        return False


# @lc code=end
