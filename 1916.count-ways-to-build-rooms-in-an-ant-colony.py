#
# @lc app=leetcode id=1916 lang=python3
#
# [1916] Count Ways to Build Rooms in an Ant Colony
#


# @lc code=start
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        graph = defaultdict(list)

        for i, v in enumerate(prevRoom):
            graph[v].append(i)

        def helper(node):
            if not graph[node]:
                return 1, 1
            c, m = 0, 1
            for neighbor in graph[node]:
                count_of_neighbors, multiplier = helper(neighbor)
                c += count_of_neighbors
                m = (m * comb(c, count_of_neighbors) * multiplier) % 1_000_000_007

            return c + 1, m

        return helper(0)[1]


# @lc code=end
