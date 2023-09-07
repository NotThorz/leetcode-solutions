#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#


# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        while a or b:
            if s[-2:] == "aa":
                s += "b"
                b -= 1
            elif s[-2:] == "bb":
                s += "a"
                a -= 1
            elif a > b:
                s += "a"
                a -= 1
            else:
                s += "b"
                b -= 1
        return s


# @lc code=end
