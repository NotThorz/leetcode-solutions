#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        d={0:0}
        ans=0
        count=0
        for i in range(n):
            count+=1 if nums[i] else -1
            if count==0:
                ans=max(ans,i+1)
            if count in d :
                ans=max(ans,i-d[count])
            else:
                d[count]=i
        return ans 

# @lc code=end

