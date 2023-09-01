#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min,second_min=float('inf'),float('inf')
        for num in nums:
            if num<=first_min:
                first_min=num
            elif num<=second_min:
                second_min=num
            else:
                return True
        return False
    #the trick here is that we find the minimum first and then we find the second minimum since we are using elif and then if we find a number bigger than the minimum and the second minumum then we have a triplet
# @lc code=end

