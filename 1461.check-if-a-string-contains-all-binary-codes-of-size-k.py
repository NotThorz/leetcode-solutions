#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(s[i : i + k] for i in range(len(s) - k + 1))) == 2**k
    #this just means we have all the binary numbers of size k which is 2**k
# @lc code=end

