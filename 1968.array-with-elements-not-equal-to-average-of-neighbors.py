#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        what we know is that the only time it is possible that an element is equal too the average of it s medians is if the element on the right is bigger and the left is smaller than the element ,so let's put elements in a way such that each element is either between two elements that are bigger than the element or two element smaller than it 
        '''
        for i in range(1, len(nums)):
            if i%2:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums

# @lc code=end

