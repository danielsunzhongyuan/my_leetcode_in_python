# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        nodes = []
        runner = head
        while runner:
            nodes.append(runner)
            runner = runner.next
        nodes = nodes[::2] + nodes[1::2]
        nodes[-1].next = None
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        return nodes[0]

