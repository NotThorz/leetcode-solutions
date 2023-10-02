#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#


# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        i = 0
        while i < len(colors):
            if colors[i] == "A":
                count = 0
                while i < len(colors) and colors[i] == "A":
                    i += 1
                    count += 1

                if count > 2:
                    alice += count - 2
            elif colors[i] == "B":
                count = 0
                while i < len(colors) and colors[i] == "B":
                    i += 1
                    count += 1

                if count > 2:
                    bob += count - 2
            else:
                i += 1

        return alice > bob


# @lc code=end
