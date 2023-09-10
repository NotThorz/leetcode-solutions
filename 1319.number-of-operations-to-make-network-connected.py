#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#


# @lc code=start
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        # Union-Find
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return True
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            return False

        components = n - 1
        for connection in connections:
            if not union(connection[0], connection[1]):
                components -= 1

        return components


# @lc code=end
