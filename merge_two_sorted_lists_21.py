# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        node1, node2 = l1, l2
        if node1.val < node2.val:
            res = l1
            node1 = node1.next
        else:
            res = l2
            node2 = node2.next
        tmp = res
        while node1 and node2:
            if node1.val < node2.val:
                tmp.next = node1
                tmp = tmp.next
                node1 = node1.next
            else:
                tmp.next = node2
                tmp = tmp.next
                node2 = node2.next
        if node1:
            tmp.next = node1
        if node2:
            tmp.next = node2
        return res
