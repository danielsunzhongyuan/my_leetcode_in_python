# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head

        nodes = []
        runner = head
        while runner:
            nodes.append(runner)
            runner = runner.next

        i, j = 0, len(nodes) - 1
        runner = ListNode(0)
        head_or_tail = True
        while i <= j:
            if head_or_tail:
                runner.next = nodes[i]
                i += 1
            else:
                runner.next = nodes[j]
                j -= 1
            runner = runner.next
            head_or_tail ^= True
        runner.next = None