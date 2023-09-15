#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#


# @lc code=start
class UF:
    def __init__(self, n):
        self.component = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        nx, ny = self.find(x), self.find(y)
        if nx == ny:
            return False
        if self.rank[nx] > self.rank[ny]:
            self.parent[ny] = nx
            self.rank[nx] += self.rank[ny]
        else:
            self.parent[nx] = ny
            self.rank[ny] += self.rank[nx]
        self.component -= 1
        return True

    def isConnected(self):
        return self.component == 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal can be solved using Prims as well , basically the min spanning tree

        n = len(points)

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(points[i], points[j])
                edges.append((dist, i, j))
        edges.sort()
        min_cost = 0
        uf = UF(n)

        return sum(cost for cost, a, b in edges if uf.union(a, b))


# @lc code=end
