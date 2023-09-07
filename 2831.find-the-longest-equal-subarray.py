#
# @lc app=leetcode id=2831 lang=python3
#
# [2831] Find the Longest Equal Subarray
#


# @lc code=start
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        start = 0
        for end in range(len(nums)):
            d[nums[end]] += 1
            ans = max(d[nums[end]], ans)
            if end - start + 1 - ans > k:
                d[nums[start]] -= 1
                start += 1
        return ans


# @lc code=end
