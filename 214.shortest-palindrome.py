#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse_s=s[::-1]
        for i in range(len(s)):
            if s.startswith(reverse_s[i:]):
                return reverse_s[:i]+s
        return reverse_s+s
# @lc code=end

