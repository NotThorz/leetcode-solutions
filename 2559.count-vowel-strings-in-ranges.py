#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#


# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        prefix = [0]
        s = 0
        ans = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            prefix.append(s)
        for start, end in queries:
            ans.append(prefix[end + 1] - prefix[start])
        return ans


# @lc code=end
