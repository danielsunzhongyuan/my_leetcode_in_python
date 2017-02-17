class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # import os
        # return os.path.abspath(path)
        stack = []
        for p in path.split("/"):
            if(p == ".."):
                if stack:
                    stack.pop()
            elif (p and p != "."):
                stack.append(p)
        return "/" + "/".join(stack)