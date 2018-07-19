# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if not head:
            return head
        while head and head.val == val:
            tmp = head
            head = head.next
            tmp.next = None
        tmp = head
        while tmp and tmp.next:
            if tmp.next.val == val:
                tmp2 = tmp.next
                tmp.next = tmp2.next
                tmp2.next = None
            else:
                tmp = tmp.next
        return head

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head.next, val)
        pre, runner = head, head
        while runner:
            if runner.val == val:
                pre.next = runner.next
            else:
                pre = runner
            runner = runner.next
        return head
