#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0 
        while i<len(nums):
            j=i
            while j<len(nums)-1:
                if nums[j]+1==nums[j+1]:
                    j+=1
                else:break
            if i!=j:
                res.append(str(nums[i])+"->"+str(nums[j]))
                i=j+1

            else:
                res.append(str(nums[i]))
                i+=1
        return res 
    



# @lc code=end

