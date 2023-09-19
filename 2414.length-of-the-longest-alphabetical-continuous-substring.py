#
# @lc app=leetcode id=2414 lang=python3
#
# [2414] Length of the Longest Alphabetical Continuous Substring
#


# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        current_length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                current_length += 1
            else:
                current_length = 1
            ans = max(ans, current_length)
        return ans


# @lc code=end
