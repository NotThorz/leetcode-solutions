#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#


# @lc code=start
class UF:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.par[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.par[px] = py


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ls = len(strs)
        uf = UF(ls)

        for i in range(ls):
            for j in range(i + 1, ls):
                if uf.find(i) == uf.find(j):
                    continue

                diff = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    uf.union(i, j)

        for i in range(ls):
            uf.find(i)

        return len(set(uf.par))


# @lc code=end
