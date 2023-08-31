#
# @lc app=leetcode id=1326 lang=python3
#
# [1326] Minimum Number of Taps to Open to Water a Garden
#

# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(len(ranges)):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        max_taps = max(dp)
        
        return max_taps if max_taps < float('inf') else -1

# @lc code=end

