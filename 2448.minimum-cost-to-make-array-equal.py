#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#


# @lc code=start
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = sorted(zip(nums, cost), key=lambda x: x[0])
        total = sum(cost)
        cnt = 0
        for num, c in nums_cost:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in nums_cost)


# @lc code=end
