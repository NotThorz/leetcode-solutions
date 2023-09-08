#
# @lc app=leetcode id=2798 lang=python3
#
# [2798] Number of Employees Who Met the Target
#


# @lc code=start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for n in hours:
            if n >= target:
                cnt += 1
        return cnt


# @lc code=end
