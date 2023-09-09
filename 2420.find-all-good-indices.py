#
# @lc app=leetcode id=2420 lang=python3
#
# [2420] Find All Good Indices
#


# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        ls, rs = -1, n

        for i in range(1, n):
            if i - ls > k:
                left[i] = 1
            if nums[i] > nums[i - 1]:
                ls = i - 1

        for j in range(n - 2, -1, -1):
            if rs - j > k:
                right[j] = 1
            if nums[j] > nums[j + 1]:
                rs = j + 1

        return [i for i in range(n) if left[i] and right[i]]


# @lc code=end
