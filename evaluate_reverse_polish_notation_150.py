# it works with Python 3, and fails with Python 2
# because with Python 2, 6 / -132 = -1, which is expected to be 0.


class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operator_priority = {
            ")": 0,
            "+": 10,
            "-": 10,
            "*": 20,
            "/": 20,
            "%": 20,
            "(": 1000
        }
        for token in tokens:
            if token in operator_priority:
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                if "*" == token:
                    stack.append(tmp1 * tmp2)
                elif "/" == token:
                    stack.append(int(tmp1 / tmp2))
                elif "+" == token:
                    stack.append(tmp1 + tmp2)
                elif "-" == token:
                    stack.append(tmp1 - tmp2)
            else:
                stack.append(int(token))
        return stack.pop()