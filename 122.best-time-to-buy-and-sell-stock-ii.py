#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                curProfit+=prices[i]-prices[i-1]
        return curProfit

# @lc code=end

