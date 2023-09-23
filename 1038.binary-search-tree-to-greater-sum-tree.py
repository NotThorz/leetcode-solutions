#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = 0

        def inorder(root):
            nonlocal val
            if root.right:
                inorder(root.right)
            root.val += val
            val = root.val
            if root.left:
                inorder(root.left)

        inorder(root)
        return root


# @lc code=end
