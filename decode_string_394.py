"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

import string


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        res = ""
        stack = []
        length = len(s)
        i = 0
        while i < length:
            if s[i] in "0123456789":
                j = i + 1
                while j < length and s[j] in "0123456789":
                    j += 1
                stack.append(int(s[i:j]))
                i = j
            elif s[i] in string.ascii_letters:
                j = i + 1
                while j < length and s[j] in string.ascii_letters:
                    j += 1
                stack.append(s[i:j])
                i = j
            elif s[i] == "[":
                stack.append(s[i])
                i += 1
            elif s[i] == "]":
                tmp = stack.pop()
                while stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()
                x = stack.pop()
                stack.append(tmp * x)
                i += 1
        while stack:
            res = stack.pop() + res
        return res


if __name__ == "__main__":
    a = Solution()
    print a.decodeString("3[a]2[bc]")
    print a.decodeString("3[a2[c]]")
    print a.decodeString("2[abc]3[cd]ef")
