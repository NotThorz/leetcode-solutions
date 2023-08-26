#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def findleft(char):
            start=0
            while start<len(s):
                if s[start]==char:
                    return start
                start+=1

        def findright(char):
            end=len(s)-1
            while end>=0:
                if s[end]==char:
                    return end
                end-=1
        s_char=set(s)
        ans=0
        for char in s_char :
            l=findleft(char)
            r=findright(char)
            ans+=len(set(s[l+1:r]))
        return ans 
        

# @lc code=end

