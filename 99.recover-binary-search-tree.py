#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder_traversal(node):
            nonlocal first, second, prev
            if not node:
                return
            
            inorder_traversal(node.left)
            
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node
            
            inorder_traversal(node.right)
        
        first, second, prev = None, None, None
        inorder_traversal(root)
        
        first.val, second.val = second.val, first.val
        
# @lc code=end

