#
# @lc app=leetcode id=2658 lang=python3
#
# [2658] Maximum Number of Fish in a Grid
#


# @lc code=start
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            if x not in range(rows) or y not in range(cols) or grid[x][y] == 0:
                return 0
            count = grid[x][y]
            grid[x][y] = 0
            count += dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
            return count

        ans = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] > 0:
                    ans = max(ans, dfs(x, y))
        return ans


# @lc code=end
