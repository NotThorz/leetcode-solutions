#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#


# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
            if len(groups[groupSizes[i]]) == groupSizes[i]:
                res.append(groups[groupSizes[i]])
                groups[groupSizes[i]] = []

        return res


# @lc code=end
