#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(head):
            fast=head
            slow=head
            prev=None
            while fast and fast.next:
                fast=fast.next.next
                prev=slow
                slow=slow.next
            if prev:
                prev.next=None
            return slow 
            
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        mid=middle(head)
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
# @lc code=end

