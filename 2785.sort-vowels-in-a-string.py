#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#


# @lc code=start
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel = []
        s = list(s)
        for i, char in enumerate(s):
            if char in vowels:
                vowel.append(char)

        vowel.sort()
        j = 0
        for i, char in enumerate(s):
            if char in vowels:
                s[i] = vowel[j]
                j += 1
        return "".join(s)


# @lc code=end
