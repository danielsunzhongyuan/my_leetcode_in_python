# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        stack = [root]
        res = []
        while stack:
            tmp = []
            for node in stack:
                if node:
                    res.append(str(node.val))
                    tmp.append(node.left)
                    tmp.append(node.right)
                else:
                    res.append("null")
            stack = tmp
        while res[-1] == "null":
            res.pop()
        return "[" + ",".join(res) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        numbers = data[1:-1].split(",")
        length = len(numbers)
        nodes = []
        for i in range(length):
            if numbers[i] != "null":
                nodes.append(TreeNode(int(numbers[i])))
            else:
                nodes.append(None)
        next_node_index = 1
        for i in range(length):
            if nodes[i]:
                if next_node_index < length:
                    nodes[i].left = nodes[next_node_index]
                    next_node_index += 1
                if next_node_index < length:
                    nodes[i].right = nodes[next_node_index]
                    next_node_index += 1
        return nodes[0] 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    codec = Codec()
    a = codec.deserialize("[5,2,3,null,null,2,4,3,1]")
    print a, a.right, a.right.left, a.right.left.left, a.right.left.right
    print codec.serialize(a)
