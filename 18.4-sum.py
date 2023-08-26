#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for l in range(n - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            
            for r in range(n - 1, l + 2, -1):
                if r < n - 1 and nums[r] == nums[r + 1]:
                    continue
                
                l1, r1 = l + 1, r - 1
                while l1 < r1:
                    total = nums[l] + nums[r] + nums[l1] + nums[r1]
                    
                    if total == target:
                        ans.append([nums[l], nums[l1], nums[r1], nums[r]])
                        while l1 < r1 and nums[l1] == nums[l1 + 1]:
                            l1 += 1
                        while l1 < r1 and nums[r1] == nums[r1 - 1]:
                            r1 -= 1
                        l1 += 1
                        r1 -= 1
                    elif total < target:
                        l1 += 1
                    else:
                        r1 -= 1
        
        return ans 
            
                
                
# @lc code=end

