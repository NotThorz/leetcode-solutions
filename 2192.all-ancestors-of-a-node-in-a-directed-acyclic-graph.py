#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#


# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[dst].append(src)

        res = []
        for i in range(n):
            stack = [i]
            ans = []
            visited = set()
            while stack:
                node = stack.pop()
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
                        ans.append(neighbor)
            res.append(sorted(ans))
        return res


# @lc code=end
