#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, value):
            if not node:
                return 0
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right) if node.val == value else 0

        self.ans = 0
        dfs(root, None)
        return self.ans


# @lc code=end
