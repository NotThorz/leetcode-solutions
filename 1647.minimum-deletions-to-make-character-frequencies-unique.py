#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#


# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        l = list(c.values())
        ans = 0
        existing = set()
        for i in range(len(l)):
            freq = l[i]
            while freq > 0 and freq in existing:
                ans += 1
                freq -= 1
            existing.add(freq)
        return ans


# @lc code=end
