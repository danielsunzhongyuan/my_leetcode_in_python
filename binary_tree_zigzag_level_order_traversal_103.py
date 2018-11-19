"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
    [3],
    [20,9],
    [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stacks = [[], []]
        stacks[0].append(root)
        res = []
        directionLtoR = True
        while stacks[0] or stacks[1]:
            currentLevelList = []
            if directionLtoR:
                while stacks[0]:
                    node = stacks[0].pop()
                    currentLevelList.append(node.val)
                    if node.left: stacks[1].append(node.left)
                    if node.right: stacks[1].append(node.right)
                directionLtoR = False
            else:
                while stacks[1]:
                    node = stacks[1].pop()
                    currentLevelList.append(node.val)
                    if node.right: stacks[0].append(node.right)
                    if node.left: stacks[0].append(node.left)
                directionLtoR = True
            res.append(currentLevelList)
        return res
