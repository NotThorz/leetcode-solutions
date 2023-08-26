#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
class UF:
    def __init__(self,n):
        self.n=n
        self.parent=[i for i in range(n+1)] # n+1 cause problem is 1 indexed
        self.rank=[1]*(n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n) 
        
        adj_list = {}
        x = y = None
        
        for src, dst in edges:
            if dst not in adj_list:
                adj_list[dst] = src
            else:
                x = adj_list[dst], dst
                y = src, dst
        
        def incycle(u, v):
            while u != v and u in adj_list:
                u = adj_list[u]
            return u == v
        
        if x and y:
            return x if incycle(*x) else y
        
        for src, dst in edges:
            if uf.union(src, dst ):  
                return [src, dst]    
# @lc code=end

