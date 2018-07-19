# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def getLength(node):
            res = 0
            runner = node
            while runner:
                res += 1
                runner = runner.next
            return res
        length = getLength(head)
        if length == 0:
            return True
        if length == 1:
            return True
        half = length / 2
        new_list = ListNode(0)
        runner = head
        i = 0
        while i < half:
            i += 1
            tmp = runner
            runner = runner.next
            tmp.next = new_list.next
            new_list.next = tmp
        if length % 2 == 0:
            return self.equal(runner, new_list.next)
        else:
            return self.equal(runner.next, new_list.next)
    
    def equal(self, node1, node2):
        while node1 and node2 and node1.val == node2.val:
            node1, node2 = node1.next, node2.next
        if not node1 and not node2:
            return True
        return False
        
