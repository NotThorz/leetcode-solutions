#
# @lc app=leetcode id=2531 lang=python3
#
# [2531] Make Number of Distinct Characters Equal
#


# @lc code=start
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        # try all possible swaps we just have at max 26 letters so worse case 26*26
        for l1 in list(c1.keys()):
            for l2 in list(c2.keys()):
                c1[l1] -= 1
                c2[l1] += 1
                if c1[l1] == 0:
                    del c1[l1]

                c2[l2] -= 1
                c1[l2] += 1
                if c2[l2] == 0:
                    del c2[l2]

                if len(c1.keys()) == len(c2.keys()):
                    return True

                c1[l1] += 1
                c2[l1] -= 1
                if c2[l1] == 0:
                    del c2[l1]
                c2[l2] += 1
                c1[l2] -= 1
                if c1[l2] == 0:
                    del c1[l2]

        return False


# @lc code=end
