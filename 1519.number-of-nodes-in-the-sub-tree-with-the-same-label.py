#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#


# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        c = defaultdict(int)
        graph = defaultdict(list)

        ans = [0] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, parent):
            lc = c[labels[node]]
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            c[labels[node]] += 1
            ans[node] = c[labels[node]] - lc

        dfs(0, -1)
        return ans


# @lc code=end
