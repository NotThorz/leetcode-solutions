#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        target = s - x
        if x > s:
            return -1
        start = 0
        window_sum = 0
        ans = float("-inf")
        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum > target:
                window_sum -= nums[start]
                start += 1
            if window_sum == target:
                ans = max(ans, end - start + 1)

        return -1 if ans == float("-inf") else len(nums) - ans


# @lc code=end
