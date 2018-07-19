class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)

    def isEmpty(self):
        if self.head.next:
            return False
        return True

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.isEmpty():
            return -1
        tmp = 0
        runner = self.head.next
        while runner.next and tmp < index:
            runner = runner.next
            tmp += 1
        if tmp == index:
            return runner.value
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = Node(val)
        if self.isEmpty():
            self.head.next = new_node
        else:
            runner = self.head.next
            while runner.next:
                runner = runner.next
            runner.next = new_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
            return
        if self.isEmpty():
            return
        tmp = 1
        runner = self.head.next
        while runner.next and tmp < index:
            runner = runner.next
            tmp += 1
        if tmp == index:
            new_node = Node(val)
            new_node.next = runner.next
            runner.next = new_node
        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.isEmpty():
            return
        pre = self.head
        runner = self.head.next
        tmp = 0
        while runner.next and tmp < index:
            pre = pre.next
            runner = runner.next
            tmp += 1
        if tmp < index:
            return
        elif tmp > index:
            self.head = self.head.next
            return
        else:
            pre.next = runner.next
            return

    def printList(self):
        runner = self.head.next
        while runner:
            print runner.value
            runner = runner.next
