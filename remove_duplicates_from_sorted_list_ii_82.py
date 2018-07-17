# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        m = {}
        runner = head
        while runner:
            m[runner.val] = m.get(runner.val, -1) + 1
            runner = runner.next
        res = head
        while res:
            if m[res.val] > 0:
                res = res.next
            else:
                break
        if not res:
            return None
        runner = res.next
        pre = res
        while runner:
            if m[runner.val] > 0:
                pre.next = runner.next
            else:
                pre = pre.next
            runner = runner.next
        return res

def buildList(arr):
    head = ListNode(0)
    for i in range(len(arr)-1, -1, -1):
        new_node = ListNode(arr[i])
        new_node.next = head.next
        head.next = new_node
    return head.next


def traverseList(head):
    runner = head
    while runner:
        print runner.val
        runner = runner.next


if __name__ == "__main__":
    s = Solution()
    head = buildList([1, 2, 3, 3, 4, 4, 5])
    res = s.deleteDuplicates(head)
    traverseList(res)

