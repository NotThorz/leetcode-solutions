#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#


# @lc code=start
class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        """
        if we are len(blocked) squares away from the source and the destination then we can reach the target cause 200 blocked
        cells can t stop us on a million by million grid so we are just checking from the source to the destination and
        from the destination to the source , if the number of cells is small between source and target then we are just
        applying a normal bfs.
        """

        escapedist = len(blocked)

        def DFS(s, t, blocked):
            nonlocal escapedist
            stk = [s]
            blocked.add(tuple(s))

            while stk:
                x, y = stk.pop()
                if abs(s[0] - x) + abs(s[1] - y) >= escapedist:
                    return True
                neigh = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
                for n in neigh:
                    if 0 <= n[0] < 1000000 and 0 <= n[1] < 1000000 and n not in blocked:
                        stk.append(n)
                        blocked.add(n)
            return (t[0], t[1]) in blocked

        blocked = {(a[0], a[1]) for a in blocked}

        return DFS(source, target, set(blocked)) and DFS(target, source, set(blocked))


# @lc code=end
