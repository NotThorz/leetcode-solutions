#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (without_current_node, with_current_node)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If the current node is robbed, the children must not be robbed.
            with_curr = node.val + left[0] + right[0]
            
            # The current node is not robbed, so the children can be either robbed or not robbed.
            without_curr = max(left) + max(right)
            
            return (without_curr, with_curr)
        
        return max(dfs(root))

            
# @lc code=end

