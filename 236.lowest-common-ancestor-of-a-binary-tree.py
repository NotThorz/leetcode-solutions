#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def traverse(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            l = traverse(node.left)
            r = traverse(node.right)
            if r and l:
                return node
            return r or l

        return traverse(root)


# @lc code=end
