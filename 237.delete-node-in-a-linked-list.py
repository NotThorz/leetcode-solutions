#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #let's copy the next node to the current node and then delete the next node since it s guarantee the node isn t a tail
        node.val=node.next.val # now our node has the value of the node that was next to it
        node.next=node.next.next #we basically deleted the next node 
# @lc code=end

