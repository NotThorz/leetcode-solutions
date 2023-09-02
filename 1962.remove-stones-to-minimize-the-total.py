#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#


# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)
        while k:
            top = heappop(heap)
            heappush(heap, top // 2)
            k -= 1
        return -sum(heap)


# @lc code=end
