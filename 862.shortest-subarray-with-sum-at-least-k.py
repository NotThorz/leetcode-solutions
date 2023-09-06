#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#


# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        q = deque()
        ans = n + 1

        for i in range(n + 1):
            while q and prefix_sum[i] - prefix_sum[q[0]] >= k:
                ans = min(ans, i - q.popleft())

            while q and prefix_sum[i] <= prefix_sum[q[-1]]:
                q.pop()

            q.append(i)

        return ans if ans <= n else -1


# @lc code=end
