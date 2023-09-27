#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#


# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for char in s:
            if char.isnumeric():
                size *= int(char)
            else:
                size += 1

        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


# @lc code=end
