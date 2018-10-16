"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return
        elif length == 1:
            return lists[0]
        elif length == 2:
            return self.mergeTwoLists(lists)
    
        B = self.mergeKLists(lists[length/2:])
        A = self.mergeKLists(lists[:length/2])
        return self.mergeTwoLists([A, B])
    
    def mergeTwoLists(self, lists):
        ret = ListNode(0)
        runner = ret
        A, B = lists[0], lists[1]
        while A and B:
            if A.val <= B.val:
                next_small = A
                A = A.next
            else:
                next_small = B
                B = B.next
            runner.next = next_small
            runner = runner.next
        while A:
            next_small = A
            A = A.next
            runner.next = next_small
            runner = runner.next
        while B:
            next_small = B
            B = B.next
            runner.next = next_small
            runner = runner.next
        return ret.next

