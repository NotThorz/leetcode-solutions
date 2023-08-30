#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert_sorted(head, node):
            if not head or head.val > node.val:
                node.next = head
                return node
            curr = head
            while curr.next and curr.next.val <= node.val:
                curr = curr.next
            node.next = curr.next
            curr.next = node
            return head

        sorted_head = None
        curr = head
        while curr:
            next_node = curr.next
            sorted_head = insert_sorted(sorted_head, curr)
            curr = next_node

        return sorted_head
# @lc code=end

