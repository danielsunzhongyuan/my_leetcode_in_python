# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre, node1, node2 = None, head, head
        tmp = 1
        while node2 and tmp < n:
            node2 = node2.next
            tmp += 1
        if tmp < n:
            return head
        while node2.next:
            pre = node1
            node1 = node1.next
            node2 = node2.next
        if not pre:
            return head.next
        pre.next = node1.next
        return head
        
    def printList(self, head):
        runner = head
        while runner:
            print runner.val
            runner = runner.next

if __name__ == "__main__":
    a = Solution()
    node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
    a.removeNthFromEnd(node1, 2)
    a.printList(node1)
