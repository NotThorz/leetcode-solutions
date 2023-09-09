#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        
        @cache
        def dfs(x,y):
            if x==n-1:
                return triangle[x][y]
            return triangle[x][y]+min(dfs(x+1,y+1),dfs(x+1,y))

        return dfs(0,0)  
# @lc code=end

