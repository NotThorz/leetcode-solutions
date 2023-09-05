#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#


# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        prefixSum = 0
        total_sum = sum(nums)

        for num in nums:
            prefixSum += num
            rightSum = total_sum - prefixSum
            res.append(abs(rightSum - prefixSum + num))

        return res


# @lc code=end
