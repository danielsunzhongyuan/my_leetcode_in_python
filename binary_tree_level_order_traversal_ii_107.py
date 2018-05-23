# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = []
        queue = [root]
        count_of_one_level = 1
        while queue:
            tmp = []
            count_of_next_level = 0
            while count_of_one_level:
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                    count_of_next_level += 1
                if node.right:
                    queue.append(node.right)
                    count_of_next_level += 1
                count_of_one_level -= 1
            count_of_one_level = count_of_next_level
            ret.append(tmp)
        return ret[::-1]
