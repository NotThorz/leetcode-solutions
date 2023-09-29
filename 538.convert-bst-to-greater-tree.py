#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
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
