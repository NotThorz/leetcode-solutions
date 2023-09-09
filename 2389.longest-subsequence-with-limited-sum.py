#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#


# @lc code=start
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        res = []
        for q in queries:
            ans = bisect_right(nums, q)
            res.append(ans)
        return res


# @lc code=end
