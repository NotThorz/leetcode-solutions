#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        start = 0
        pre = 0
        for end in range(len(nums)):
            pre += nums[end]
            while pre * (end - start + 1) >= k:
                pre -= nums[start]
                start += 1
            ans += end - start + 1
        return ans


# @lc code=end
