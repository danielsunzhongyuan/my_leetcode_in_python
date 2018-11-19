class Solution(object):
    def __init__(self):
        self.operator_priority = {
            ")": 0,
            "+": 10,
            "-": 10,
            "*": 20,
            "/": 20,
            "%": 20,
            "(": 1000
        }

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        reverse_polish = self.reverse_polish_notation(s)
        return self.calculate_by_reverse_polish(reverse_polish)

    def reverse_polish_notation(self, s):
        res = []
        i = 0
        stack = []
        length = len(s)
        while i < length:
            if s[i] in self.operator_priority:
                if not stack:
                    stack.append(s[i])
                else:
                    if self.operator_priority[s[i]] > self.operator_priority[stack[-1]]:
                        stack.append(s[i])
                    else:
                        while stack and self.operator_priority[s[i]] <= self.operator_priority[stack[-1]] \
                                and stack[-1] != "(":
                            res.append(stack.pop())
                        if ")" == s[i]:
                            stack.pop()
                        else:
                            stack.append(s[i])
                i += 1
            elif s[i] in "0123456789":
                tmp = i + 1
                while tmp < length and s[tmp] in "0123456789":
                    tmp += 1
                res.append(s[i:tmp])
                i = tmp
            else:
                i += 1
        while stack:
            res.append(stack.pop())
        return res

    def calculate_by_reverse_polish(self, tokens):
        stack = []
        for token in tokens:
            if token in self.operator_priority:
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                if "*" == token:
                    stack.append(tmp1 * tmp2)
                elif "/" == token:
                    stack.append(tmp1 / tmp2)
                elif "+" == token:
                    stack.append(tmp1 + tmp2)
                elif "-" == token:
                    stack.append(tmp1 - tmp2)
            else:
                stack.append(int(token))
        return stack.pop()
