"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        res = []
        self.traverse(res, head)
        if len(res) == 1:
            return head
        res[0].prev = res[0].child = None
        res[0].next = res[1]
        for i in range(1, len(res) - 1):
            res[i].next = res[i+1]
            res[i].prev = res[i-1]
            res[i].child = None
        res[-1].prev = res[-2]
        res[-1].next = res[-1].child = None
        return res[0]
        
    def traverse(self, res, node):
        if not node:
            return
        res.append(node)
        self.traverse(res, node.child)
        self.traverse(res, node.next)


class Solution2(object):
    def flatten(self, head):
        # Initialize the current reference and stack of saved next pointers
        curr, tempStack = head, [];
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    tempStack.append(curr.next);
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None;
            if not curr.next and len(tempStack):
                # If the current node is a child without a next pointer
                temp = tempStack.pop();
                # Current <-> Temp
                temp.prev, curr.next = curr, temp;
            curr = curr.next;
        return head;
