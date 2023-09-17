#
# @lc app=leetcode id=1927 lang=python3
#
# [1927] Sum Game
#


# @lc code=start
class Solution:
    def sumGame(self, num: str) -> bool:
        # o(N)
        bob = 0  # sum bob count
        bob_open = 0  # number of ? in bob side
        for i in range(len(num) // 2):
            if num[i] == "?":
                bob_open += 1
            else:
                bob += int(num[i])

        alice = 0  # sum alice count
        alice_open = 0  # number of ? in  alice side
        for i in range(len(num) // 2, len(num)):
            if num[i] == "?":
                alice_open += 1
            else:
                alice += int(num[i])

        if (alice_open + bob_open) % 2 == 1:
            return True  # alice always wins cause she has the last move
        # in the case the ? is even
        sum_diff = (
            bob - alice
        )  # the difference of the sums ,positive if bob has more open spots
        question_mark_diff = (
            alice_open - bob_open
        )  # the difference of the ? , positive if alice has more open spots
        return not (question_mark_diff // 2 * 9 == sum_diff)  # some math equation xd


# @lc code=end
