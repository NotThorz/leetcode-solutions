#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        count=Counter(s)
        is_odd=0
        for i in count:
            if count[i]%2==1:
                is_odd+=1
        return n-is_odd+1 if is_odd>1 else n
# @lc code=end

