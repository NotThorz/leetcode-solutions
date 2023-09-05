#
# @lc app=leetcode id=2640 lang=python3
#
# [2640] Find the Score of All Prefixes of an Array
#


# @lc code=start
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_pre = [nums[0]]
        m = nums[0]
        n = len(nums)
        for i in range(1, n):
            if m < nums[i]:
                m = nums[i]
            max_pre.append(m)
        res = []
        s = 0
        for i in range(n):
            s += nums[i] + max_pre[i]
            res.append(s)
        return res


# @lc code=end
