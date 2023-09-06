#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#


# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        pre = 0
        res = 0
        for num in nums:
            pre += num
            if pre % k == 0:
                res += 1
            res += count[pre % k]
            count[pre % k] += 1
        return res


# @lc code=end
