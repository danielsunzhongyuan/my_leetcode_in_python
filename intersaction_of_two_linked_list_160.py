# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA and not headB:
            return None
        runnerA, runnerB = headA, headB
        while runnerA != runnerB:
            runnerA = runnerA.next if runnerA else headB
            runnerB = runnerB.next if runnerB else headA
        return runnerA
