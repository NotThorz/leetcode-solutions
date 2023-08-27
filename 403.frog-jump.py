#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Create a dictionary to store possible jump lengths at each stone position
        # The key is the stone position and the value is a set of possible jump lengths
        jump_dict = {stone: set() for stone in stones}
        jump_dict[0].add(1)  # The frog can jump 1 unit from the start
        
        for stone in stones:
            for jump in jump_dict[stone]:
                if jump > 1:  # Jump back
                    if stone + jump - 1 in jump_dict:
                        jump_dict[stone + jump - 1].add(jump - 1)
                if stone + jump in jump_dict:
                    jump_dict[stone + jump].add(jump)
                if stone!=0 and stone + jump + 1 in jump_dict:
                    jump_dict[stone + jump + 1].add(jump + 1)
        
        return len(jump_dict[stones[-1]]) > 0


# @lc code=end

