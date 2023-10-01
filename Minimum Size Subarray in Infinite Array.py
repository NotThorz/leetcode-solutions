class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        times = target // sum(nums) + 2
        infinite_nums = nums * times

        left = 0
        currentSum = 0
        minLength = float('inf')

        for right in range(len(infinite_nums)):
            currentSum += infinite_nums[right]

            while currentSum >= target:
                if currentSum == target:
                    minLength = min(minLength, right - left + 1)
                currentSum -= infinite_nums[left]
                left += 1

        return minLength if minLength != float('inf') else -1