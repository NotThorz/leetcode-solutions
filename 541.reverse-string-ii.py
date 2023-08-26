#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=list(s)
        for i in range(0,len(s),k*2):
            a[i:i+k]=a[i:i+k][::-1]
        return "".join(a)
            
# @lc code=end

