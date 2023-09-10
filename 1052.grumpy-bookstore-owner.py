#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#


# @lc code=start
class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        if minutes >= len(customers):
            return sum(customers)

        ans = sum(customers[:minutes]) + sum(
            [customers[i] for i in range(minutes, len(customers)) if grumpy[i] == 0]
        )
        curr = ans
        start = 0

        for end in range(minutes, len(customers)):
            if grumpy[start] == 1:
                curr -= customers[start]
            if grumpy[end] == 1:
                curr += customers[end]
            start += 1
            ans = max(ans, curr)

        return ans


# @lc code=end
