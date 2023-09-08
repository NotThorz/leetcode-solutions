#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if sum(nums[:3]) > target:
            return sum(nums[:3])
        if sum(nums[-3:]) < target:
            return sum(nums[-3:])
        n = len(nums)
        res = float("inf")
        for l in range(n - 2):
            mid, r = l + 1, n - 1
            while mid < r:
                if abs(nums[l] + nums[mid] + nums[r] - target) < abs(res - target):
                    res = nums[l] + nums[mid] + nums[r]

                if nums[l] + nums[mid] + nums[r] < target:
                    mid += 1
                else:
                    r -= 1
        return res


# @lc code=end
