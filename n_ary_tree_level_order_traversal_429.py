"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            tmp = []
            res.append([node.val for node in stack])
            for node in stack:
                for child_node in node.children:
                    tmp.append(child_node)
            stack = tmp
        return res
