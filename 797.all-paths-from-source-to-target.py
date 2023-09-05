#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adj_list = defaultdict(list)
        for src, dst in enumerate(graph):
            adj_list[src] = dst
        res = []
        q = deque([(0, [0])])
        while q:
            node, path = q.popleft()
            if node == n - 1:
                res.append(path)

            for neighbor in graph[node]:
                q.append((neighbor, path.copy() + [neighbor]))
        return res


# @lc code=end
