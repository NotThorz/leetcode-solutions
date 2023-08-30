#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#

# @lc code=start
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len( nums )
        ans=0
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                continue
            number_of_elements=(nums[i+1]+nums[i]-1)//nums[i+1]
            ans+=number_of_elements-1
            nums[i]=nums[i]//number_of_elements
        return ans             
#what we are doing is basically starting from the end , if a number is bigger than the one succeeding it(reading left to right)
#we divide it until it reaches the num succeding it and we do that for the whole array    
# @lc code=end

