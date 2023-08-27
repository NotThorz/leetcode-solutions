#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        len_window=0
        i=0
        ans=0
        while i<len(nums):
            if nums[i]==0:
                len_window+=1
                ans+=len_window
            else:
                len_window=0
            i+=1
        return ans 
    #U can find the math way that proves this in my previous submition 
# @lc code=end

