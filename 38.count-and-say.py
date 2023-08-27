#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
    
        prev_term = self.countAndSay(n - 1)
        
        new_term = ""
        count = 1
        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                new_term += str(count) + prev_term[i - 1]
                count = 1
        new_term += str(count) + prev_term[-1]
        
        return new_term
# @lc code=end

