#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count=0
        L_count=0
        for char in s :
            if char=="A":
                A_count+=1
                if A_count>1:
                    return False
            if char=="L":
                L_count+=1
                if L_count>2:
                    return False
            else:
                L_count=0
        return True  


# @lc code=end

