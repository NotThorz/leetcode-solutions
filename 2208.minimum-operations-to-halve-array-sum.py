#
# @lc app=leetcode id=2208 lang=python3
#
# [2208] Minimum Operations to Halve Array Sum
#


# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        half = s / 2
        heap = [-n for n in nums]
        heapify(heap)
        ans = 0
        while s > half:
            ans += 1
            top = -heappop(heap)
            s -= top / 2
            heappush(heap, -top / 2)
        return ans


# @lc code=end
