# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        new_head = ListNode(0)
        runner = head
        while runner:
            tmp = runner
            runner = runner.next
            tmp.next = new_head.next
            new_head.next = tmp
        return new_head.next
