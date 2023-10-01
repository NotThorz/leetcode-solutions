class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], nums[i])

        max_triplet = 0
        for i in range(1, n - 1):
            left_val = left[i - 1]
            right_val = right[i + 1]
            trip = (left_val - nums[i]) * right_val
            max_triplet = max(max_triplet, trip)

        return max(max_triplet, 0)