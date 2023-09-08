#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#


# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols, cells, res = len(grid), len(grid[0]), 1, 0

        def dfs(x, y, count, visited):
            nonlocal res
            if (
                x not in range(rows)
                or y not in range(cols)
                or grid[x][y] == -1
                or (x, y) in visited
            ):
                return

            if grid[x][y] == 2:
                if count == cells:
                    res += 1
                return

            visited.add((x, y))
            dfs(x + 1, y, count + 1, visited)
            dfs(x - 1, y, count + 1, visited)
            dfs(x, y + 1, count + 1, visited)
            dfs(x, y - 1, count + 1, visited)
            visited.remove((x, y))

        startX, startY = 0, 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    startX, startY = x, y
                if grid[x][y] == 0:
                    cells += 1
        dfs(startX, startY, 0, set())
        return res


# @lc code=end
