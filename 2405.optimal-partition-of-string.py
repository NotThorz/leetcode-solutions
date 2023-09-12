#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        ans=1
        se=set()
        for char in s :
            if char not in se:
                se.add(char)
            else:
                ans+=1
                se=set()
                se.add(char)
        return ans
# @lc code=end

