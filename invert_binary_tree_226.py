# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Solution One
        # if not root:
        #     return root
        # elif not root.left and not root.right:
        #     return root
        # elif not root.left and root.right:
        #     root.left = root.right
        #     root.right = None
        #     self.invertTree(root.left)
        # elif root.left and not root.right:
        #     root.right = root.left
        #     root.left = None
        #     self.invertTree(root.right)
        # elif root.left and root.right:
        #     tmp = root.right
        #     root.right = root.left
        #     root.left = tmp
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root

        # Solution Two
        # if root != None:
        #     root.left, root.right = root.right, root.left
        #     map(self.invertTree, (root.left, root.right))
        # return root

        # Solution Three
        if root != None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

        # Solution Four
        # queue = collections.deque([(root)])
        # while queue:
        #     node = queue.popleft()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)
        # return root

        # Solution Five
        # stack = [root]
        # while stack:
        #     x = stack.pop()
        #     if x:
        #         x.left, x.right = x.right, x.left
        #         # stack.append(x.left)
        #         # stack.append(x.right)
        #         stack.extend([x.left, x.right])
        # return root
