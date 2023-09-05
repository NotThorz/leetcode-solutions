#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#


# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)

        res = [0] * len(nums)
        for num, val in d.items():
            suffixSum = sum(val)
            preffixSum = 0
            s = len(val)
            p = 0
            for i in val:
                preffixSum += i
                p += 1
                suffixSum -= i
                s -= 1
                res[i] = -preffixSum + p * i - s * i + suffixSum
        return res


# @lc code=end
