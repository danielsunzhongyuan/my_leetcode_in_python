# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parent = {}
        visited = {}
        def dfs(pre, cur, parent, visited):
            if not cur:
                return
            parent[cur] = pre
            visited[cur] = False
            dfs(cur, cur.left, parent, visited)
            dfs(cur, cur.right, parent, visited)
        dfs(None, root, parent, visited)
        queue = []
        distance = 0
        queue.append(target)
        while queue:
            if distance == K:
                break
            tmp = []
            for node in queue:
                visited[node] = True
                if node.left and visited[node.left] == False:
                    tmp.append(node.left)
                    visited[node.left] = True
                if node.right and visited[node.right] == False:
                    tmp.append(node.right)
                    visited[node.right] = True
                if parent[node] and visited[parent[node]] == False:
                    tmp.append(parent[node])
                    visited[parent[node]] = True
            queue = tmp
            distance += 1
        return [node.val for node in queue]