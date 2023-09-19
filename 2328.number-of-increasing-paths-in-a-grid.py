#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#


# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            paths = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > grid[x][y]:
                    paths += dfs(nx, ny)

            memo[(x, y)] = (paths + 1) % mod
            return memo[(x, y)]

        ans = 0
        for x in range(rows):
            for y in range(cols):
                ans = (ans + dfs(x, y)) % mod

        return ans


# @lc code=end
