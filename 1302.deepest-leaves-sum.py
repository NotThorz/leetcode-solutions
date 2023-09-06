#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            row = 0
            for _ in range(len(q)):
                node = q.popleft()
                row += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans = row
        return ans


# @lc code=end
