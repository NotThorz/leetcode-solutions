#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_penalty, min_penalty = 0, 0
        ans = 0

        for i, ch in enumerate(customers):

            if ch == "Y":
                current_penalty -= 1
            else:
                current_penalty += 1

            if current_penalty < min_penalty:
                ans = i + 1
                min_penalty = current_penalty

        return ans
# @lc code=end

