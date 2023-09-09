#
# @lc app=leetcode id=2100 lang=python3
#
# [2100] Find Good Days to Rob the Bank
#


# @lc code=start
class Solution:
    def goodDaysToRobBank(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1

        for j in range(n - 2, -1, -1):
            if nums[j] <= nums[j + 1]:
                right[j] = right[j + 1] + 1

        return [i for i in range(n) if left[i] >= k and right[i] >= k]


# @lc code=end
