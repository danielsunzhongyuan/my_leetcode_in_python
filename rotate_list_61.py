# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = self.getLength(head)
        if length <= 1: return head
        k = k % length
        if k <= 0: return head
        original_head = original_end = new_head = new_end = head
        while k > 0:
            original_end = original_end.next
            k -= 1
        while original_end.next:
            new_end = new_end.next
            original_end = original_end.next
        new_head = new_end.next
        original_end.next = original_head
        new_end.next = None
        return new_head

    def getLength(self, node):
        res = 0
        tmp = node
        while tmp:
            tmp = tmp.next
            res += 1
        return res

