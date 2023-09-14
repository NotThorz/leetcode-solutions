#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#


# @lc code=start
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # bfs with binary search
        cells = list(map(tuple, cells))

        def search(day):
            queue = deque([(1, i) for i in range(1, col + 1)])
            visited = set(cells[:day])
            while queue:
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if not (1 <= r <= row and 1 <= c <= col):
                    continue
                if r == row:
                    return 0
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    queue.append((r + dr, c + dc))
            return 1

        return bisect.bisect(range(1, len(cells)), 0, key=search)


# @lc code=end
