#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        curr=l1
        while curr:
            s1+=str(curr.val)
            curr=curr.next
        curr=l2
        while curr:
            s2+=str(curr.val)
            curr=curr.next
        s3=str(int(s1)+int(s2))
        dummy=ListNode(0)
        curr=dummy
        for char in s3:
            node=ListNode(int(char))
            curr.next=node
            curr=curr.next
        return dummy.next

# @lc code=end

