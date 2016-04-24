class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesesMap = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if not stack:
                    return False
                last = stack.pop()
                if parenthesesMap.get(last, "") == c:
                    continue
                else:
                    return False
            else:
                continue
        if stack:
            return False
        return True
