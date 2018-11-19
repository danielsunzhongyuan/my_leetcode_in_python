# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #         if not root:
        #             return
        #         nodes = []
        #         self.preorder_traverse(nodes, root)
        #         for i in range(len(nodes)-1):
        #             nodes[i].left = None
        #             nodes[i].right = nodes[i+1]
        #         nodes[-1].left = None
        #         nodes[-1].right = None

        #     def preorder_traverse(self, nodes, node):
        #         if not node:
        #             return
        #         nodes.append(node)
        #         self.preorder_traverse(nodes, node.left)
        #         self.preorder_traverse(nodes, node.right)
        self.helper(root, None)

    def helper(self, root, tail):
        if not root:
            return tail

        root.right = self.helper(root.left, self.helper(root.right, tail))
        root.left = None
        return root
