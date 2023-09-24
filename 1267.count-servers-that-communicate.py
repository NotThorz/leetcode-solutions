#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        ans = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]:
                    row_count[x] += 1
                    col_count[y] += 1

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] and (row_count[x] > 1 or col_count[y] > 1):
                    ans += 1

        return ans

# @lc code=end

