# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next:
            return False

        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
