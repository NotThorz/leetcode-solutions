#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x :x[1])
        curr=float('-inf')
        counter=0
        for pair in pairs:
            if pair[0]>curr:
                counter+=1
                curr=pair[1]
        return counter 
# @lc code=end

