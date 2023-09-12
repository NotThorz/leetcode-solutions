#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)


# @lc code=end
