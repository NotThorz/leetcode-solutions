#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min=left_max=0

        for char in s:
            if char=='(':
                left_min+=1
                left_max+=1
            elif char==')':
                left_min=max(left_min-1,0) #if negative reset to 0
                left_max-=1
            else:
                #wildcard , we count it as a ( for max and ) for min
                left_min=max(left_min-1,0)
                left_max+=1
            if left_max<0:
                return False
        return left_min==0
# @lc code=end

