# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         if root is None:
#             return root
#         def helper(node, pre, parent, depth):
#             if node is None:
#                 return
#             parent[node] = pre
#             depth[node] = depth.get(pre, 0) + 1
#             helper(node.left, node, parent, depth)
#             helper(node.right, node, parent, depth)
#         parent = {}
#         depth = {}
#         helper(root, None, parent, depth)
#         tmp = sorted(depth.items(), key=lambda x:x[1], reverse=True)
#         current_nodes = [x[0] for x in tmp if x[1] == tmp[0][1]]
#         print current_nodes
#         while current_nodes and len(current_nodes) > 1:
#             tmp = [parent[node] for node in current_nodes if parent[node] is not None]
#             current_nodes = list(set(tmp))
#         return current_nodes[0]

        self.ret = None
        self.depth = 0
        def dfs(head, dep):
            if head == None:
                return dep, None
            dep += 1
            l = dfs(head.left, dep)
            r = dfs(head.right, dep)
            if l[0] > r[0]:
                return l[0], l[1]
            elif l[0] < r[0]:
                return r[0], r[1]
            else:
                return l[0], head
            # if m >= self.depth:
            #     self.depth = m
            #     if l == r:
            #         self.ret = head
            # return m
        return dfs(root, 0)[1]
