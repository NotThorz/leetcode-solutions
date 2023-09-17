#
# @lc app=leetcode id=2023 lang=python3
#
# [2023] Number of Pairs of Strings With Concatenation Equal to Target
#


# @lc code=start
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c = Counter(nums)
        ans = 0
        for k, v in c.items():
            if target.startswith(k):
                suffix = target[len(k) :]
                ans += v * c[suffix]
                if k == suffix:
                    ans -= c[suffix]
        return ans


# @lc code=end
