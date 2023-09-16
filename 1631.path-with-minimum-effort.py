#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Modified Dijkstra
        rows,cols=len(heights),len(heights[0])
        def paths(x,y):
            paths=[(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i,j in paths:
                yield (x+i,y+j)
        def isValid(x,y):
            return x in range(rows) and y in range(cols)
        efforts={(i,j): float('inf') for i in range(rows) for j in range(cols)}
        efforts[(0,0)]=0

        heap=[(0,0,0)]

        while heap:
            effort,row,col=heappop(heap)
            if row==rows-1 and col==cols-1:
                return effort
            for x,y in paths(row,col):
                if isValid(x,y):
                    new=max(effort,abs(heights[row][col]-heights[x][y]))
                    if new<efforts[(x,y)]:
                        efforts[(x,y)]=new
                        heappush(heap,(new,x,y))
# @lc code=end

