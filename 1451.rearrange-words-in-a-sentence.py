#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        s = text.split()
        s[0] = s[0].lower()
        s.sort(key=lambda x: len(x))
        s[0] = s[0].capitalize()
        return " ".join(s)

# @lc code=end

