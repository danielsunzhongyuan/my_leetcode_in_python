# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Solution One: 99ms
        # stack = [root]
        # parent = {root: None}
        # while p not in parent or q not in parent:
        #     node = stack.pop()
        #     if node.left:
        #         parent[node.left] = node
        #         stack.append(node.left)
        #     if node.right:
        #         parent[node.right] = node
        #         stack.append(node.right)
        # ancestor_of_p = []
        # while p:
        #     ancestor_of_p.append(p)
        #     p = parent[p]
        # while q not in ancestor_of_p:
        #     q = parent[q]
        # return q

        # Solution Two:
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestor_of_p = []
        while p:
            ancestor_of_p.append(p)
            p = parent[p]
        while q not in ancestor_of_p:
            q = parent[q]
        return q
