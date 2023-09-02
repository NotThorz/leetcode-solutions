#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#


# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        ans = 0
        while k:
            n = -heappop(heap)
            ans += n
            heappush(heap, -ceil(n / 3))
            k -= 1
        return ans


# @lc code=end
