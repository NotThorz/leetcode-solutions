#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if indexDiff < 0 or valueDiff < 0:
            return False
        s = SortedSet()
        for end in range(len(nums)):
            floor = s.bisect_left(nums[end])
            if floor != len(s) and abs(s[floor] - nums[end]) <= valueDiff:
                return True
            ceil = s.bisect_left(nums[end] - valueDiff)
            if ceil != len(s) and abs(s[ceil] - nums[end]) <= valueDiff:
                return True
            s.add(nums[end])
            if end >= indexDiff:
                s.remove(nums[end - indexDiff])
        return False


# @lc code=end
