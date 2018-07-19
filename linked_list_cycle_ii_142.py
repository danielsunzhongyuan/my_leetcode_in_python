# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return None
        
        slow, fast = head.next, head.next.next
        while slow!=fast:
            if not fast or not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
        
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
        
