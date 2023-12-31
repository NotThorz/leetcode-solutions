#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = None
        self.min_diff = float('inf')
        
        def inorder_traversal(node):
            if not node:
                return
            
            inorder_traversal(node.left)
            
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
            self.prev_val = node.val
            
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.min_diff

# @lc code=end

