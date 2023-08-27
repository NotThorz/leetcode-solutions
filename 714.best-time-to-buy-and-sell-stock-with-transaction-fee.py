#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = -prices[0]
        sell = 0
        
        for i in range(1, n):
            prev_buy = buy
            buy = max(buy, sell - prices[i])
            sell = max(sell, prev_buy + prices[i] - fee)
        
        return sell

# @lc code=end

