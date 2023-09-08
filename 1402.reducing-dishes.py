#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#


# @lc code=start
class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort(reverse=True)
        prefix = 0
        ans = 0
        for i in range(len(s)):
            if prefix + s[i] > 0:
                prefix += s[i]
                ans += prefix
        return ans


# @lc code=end
