#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if not node:
                return 0
            else:
                return 1 + max(get_height(node.left), get_height(node.right))

        h = get_height(root)
        rows = h
        cols = 2 ** (h) - 1
        mat = [["" for _ in range(cols)] for _ in range(rows)]

        if not root:
            return mat

        def place(node, row, start, end):
            if not node:
                return
            mid = (start + end) // 2
            mat[row][mid] = str(node.val)
            place(node.left, row + 1, start, mid - 1)
            place(node.right, row + 1, mid + 1, end)

        place(root, 0, 0, cols - 1)
        return mat


# @lc code=end
