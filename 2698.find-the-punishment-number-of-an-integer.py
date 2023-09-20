#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#


# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def valid(s, target):
            if len(s) == 0 and target == 0:
                return True

            if target < 0:
                return False

            ans = False
            for i in range(len(s)):
                left_part = s[0 : i + 1]
                right_part = s[i + 1 :]
                if valid(right_part, target - int(left_part)):
                    return True
            return ans

        ans = 0
        for i in range(1, n + 1):
            if valid(str(i * i), i):
                ans += i * i
        return ans


# @lc code=end
