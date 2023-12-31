#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = str(root.val)
        if root.left and not root.right:
            s += "(" + self.tree2str(root.left) + ")"
        if root.right:
            s += "(" + self.tree2str(root.left) + ")"
            s += "(" + self.tree2str(root.right) + ")"
        return s


# @lc code=end
