#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0:
                res[i - 1] += "Fizz"
            if i % 5 == 0:
                res[i - 1] += "Buzz"
            if not res[i - 1]:
                res[i - 1] = str(i)
        return res


# @lc code=end
