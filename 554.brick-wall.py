#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        index_to_count = defaultdict(int)
        max_count = 0  # Tracks the maximum number of crossings

        for row in wall:
            position = 0
            for brick in row[:-1]: # we dont take the last position since it s an edge which means it will have the max amount of gaps but the problem tells us to not return the edges 0 and len(wall)-1
                position += brick
                index_to_count[position] += 1
                max_count = max(max_count, index_to_count[position])

        return len(wall) - max_count
    #WE are basically counting the gaps , so in each position we add the len of the brick and that just tells us there is a gap there , and then we know that the place that has the maximum amount of gaps is actually the place where we will cross the minimum walls which means we return len(wall)- max (index_to_count.values)  but we keep track of the max in a variable for less time complexity .

                


# @lc code=end

