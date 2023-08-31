#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start=0
        max_val=float('-inf')
        end=float('inf')
        heap=[]
        for i in range(len(nums)):
            heappush(heap,(nums[i][0],i,0))
            max_val=max(max_val,nums[i][0])
        
        while True:
            min_val,line,col=heappop(heap)
            if end-start>max_val-min_val:
                end=max_val
                start=min_val
            next_col=col+1
            if next_col==len(nums[line]):
                break
            heappush(heap,(nums[line][next_col],line,next_col))
            max_val=max(max_val,nums[line][next_col])
        return [start,end]
# @lc code=end

