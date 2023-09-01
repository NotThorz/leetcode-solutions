#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        empty=0
        max_distance=0

        #the case where the best solution is in the middle
        #[0,1,0,0,0,1,0,1]
        for seat in seats:
            if seat:
                empty=0
            else:
                empty+=1
                max_distance=max(max_distance,(empty+1)//2)
        
        #the case where empty seats are in the end [1,0,0,0,0,0]
        max_distance=max(max_distance,empty)
        #the case where empty seats at the beginning [0,0,0,0,1,0,1]
        max_distance=max(max_distance,seats.index(1))

        return max_distance
# @lc code=end

