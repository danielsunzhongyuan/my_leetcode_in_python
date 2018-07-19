# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            tmp = []
            length = len(stack)
            for i in range(length):
                if i == length - 1:
                    stack[i].next = None
                else:
                    stack[i].next = stack[i+1]
                if stack[i].left:
                    tmp.append(stack[i].left)
                if stack[i].right:
                    tmp.append(stack[i].right)
            stack = tmp
        return
