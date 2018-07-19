# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        nxtRet = ret
        node1, node2 = l1, l2
        nxtRet.val = (node1.val+node2.val)%10
        carry = (node1.val+node2.val)/10
        node1=node1.next
        node2=node2.next
        while node1 and node2:
            newNode = ListNode(0)
            newNode.val = (node1.val+node2.val+carry)%10
            newNode.next = None
            nxtRet.next = newNode
            nxtRet = newNode
            carry = (node1.val+node2.val+carry)/10
            node1 = node1.next
            node2 = node2.next
            
        if node2:
            while node2:
                newNode = ListNode(0)
                newNode.val = (node2.val+carry)%10
                newNode.next = None
                nxtRet.next = newNode
                nxtRet = newNode
                carry = (node2.val+carry)/10
                node2 = node2.next
            
        elif node1:
            while node1:
                newNode = ListNode(0)
                newNode.val = (node1.val+carry)%10
                newNode.next = None
                nxtRet.next = newNode
                nxtRet = newNode
                carry = (node1.val+carry)/10
                node1 = node1.next
            
        if carry:
            newNode = ListNode(1)
            nxtRet.next = newNode
        return ret
            
