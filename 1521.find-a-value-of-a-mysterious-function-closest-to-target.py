#
# @lc app=leetcode id=1521 lang=python3
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#


# @lc code=start
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s = set()
        ans = float("inf")
        for i in range(len(arr)):
            ns = set()
            ns.add(arr[i])
            for num in s:
                ns.add(num & arr[i])
            for num in ns:
                ans = min(ans, abs(target - num))
            s = ns
        return ans


# @lc code=end
